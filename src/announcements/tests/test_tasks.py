from django.contrib.auth import get_user_model

from model_bakery import baker
from tenant_schemas.test.cases import TenantTestCase

from siteconfig.models import SiteConfig

from announcements import tasks
from announcements.models import Announcement

User = get_user_model()


class AnnouncementTasksTests(TenantTestCase):
    """ Run tasks asyncronously with apply() """

    def setUp(self):
        self.announcement = baker.make(Announcement)

        # need a teacher before students can be created or the profile creation will fail when trying to notify
        self.test_teacher = User.objects.create_user('test_teacher', is_staff=True)
        self.test_student1 = User.objects.create_user('test_student')
        self.test_student2 = baker.make(User)

        self.ai_user, _ = User.objects.get_or_create(
            pk=SiteConfig.get().deck_ai.pk,
            defaults={
                'username': "Autogenerated AI",
            },
        )

    def test_send_announcement_emails(self):
        task_result = tasks.send_announcement_emails.apply(
            kwargs={
                "content": "", 
                "root_url": "https://example.com", 
                "absolute_url": "/link/to/announcement/"
            }
        )
        self.assertTrue(task_result.successful())

    def test_publish_announcement(self):
        self.assertTrue(self.announcement.draft)
        task_result = tasks.publish_announcement.apply(
            kwargs={
                'user_id': self.test_teacher.id,
                'announcement_id': self.announcement.id,
                'root_url': "https://example.com"
            }
        )
        self.assertTrue(task_result.successful())

        # Make sure the announcement is no longer a draft
        # get updated instance of announcement
        no_longer_draft_announcement = Announcement.objects.get(pk=self.announcement.pk)
        self.assertFalse(no_longer_draft_announcement.draft)

    def test_send_notifications(self):

        tasks.send_notifications(self.ai_user.id, self.announcement.id)

        # run method as synchronous task
        task_result = tasks.send_notifications.apply(
            kwargs={
                'user_id': self.ai_user.id,  # self.test_teacher.id,
                'announcement_id': self.announcement.id
            })
        self.assertTrue(task_result.successful())
