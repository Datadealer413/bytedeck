# Generated by Django 2.2.24 on 2022-01-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0005_auto_20200813_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='max_active_users',
            field=models.SmallIntegerField(default=40, help_text='The maximum number of users that can be active on this deck; -1 = unlimited.'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='max_quests',
            field=models.SmallIntegerField(default=100, help_text='The maximum number of quests that can be active on this deck (archived quests are considered inactive); -1 = unlimited.'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='owner_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='owner_full_name',
            field=models.CharField(blank=True, help_text='The owner of this deck.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='paid_until',
            field=models.DateField(blank=True, help_text='If the deck is not in trial mode, then the deck will become inaccessable to students after this date.', null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='trial_end_date',
            field=models.DateField(blank=True, help_text='The date when the trial period ends. Blank or a date in the past means the deck is not in trial mode.', null=True),
        ),
    ]
