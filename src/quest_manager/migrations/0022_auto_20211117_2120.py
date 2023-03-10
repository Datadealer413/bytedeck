# Generated by Django 2.2.24 on 2021-11-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_manager', '0021_auto_20211117_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='xp_can_be_entered_by_students',
            field=models.BooleanField(default=False, help_text='Allow students to enter a custom XP value for their submission of this quest.'),
        ),
        migrations.AddField(
            model_name='questsubmission',
            name='xp_requested',
            field=models.PositiveIntegerField(default=0, help_text='The number of XP you requesting for this quest submission.'),
        ),
    ]
