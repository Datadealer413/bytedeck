from django.db.models.signals import post_save
from django.dispatch import receiver

from django_celery_beat.models import ClockedSchedule, PeriodicTask

from djconfig import config, reload_maybe

from .models import Announcement
# from .tasks import send_announcement_emails


@receiver(post_save, sender=Announcement)
def save_announcement_signal(sender, instance, **kwargs):
    """ After an announcement is saves, check if it's a draft and that it should auto-publish the results.
    If it should, then check if there is already a beat task scheduled and replace it, or create a new schedule
    """

    task_name = "Autopublication task for announcement #{}".format(instance.id)

    if instance.draft and instance.auto_publish:

        reload_maybe()  # djconfig for "AI" user

        schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=instance.datetime_released
        ) 

        # PeriodicTask doesn't have an update_or_create method for some reason, so do it long way
        # https://github.com/celery/django-celery-beat/issues/106
        defaults = {
            'clocked': schedule,
            'task': 'notifications.tasks.publish_announcement',
            'queue': 'default',
            'kwargs': {
                'user_id': config.hs_hackerspace_ai,
                'announcement_id': instance.id,
                'absolute_url': instance.get_absolute_url(),
            },
            'one_off': True,
            'enabled': True,
        }
        try:
            task = PeriodicTask.objects.get(name=task_name)
            for key, value in defaults.items():
                setattr(task, key, value)
            task.save()
        except PeriodicTask.DoesNotExist:
            new_values = {'name': task_name}
            new_values.update(defaults)
            task = PeriodicTask(**new_values)
            task.save()

    else:  # There shouldn't be a task so delete if it exists
        try:
            task = PeriodicTask.objects.get(name=task_name)
            task.delete()
        except PeriodicTask.DoesNotExist:
            pass
