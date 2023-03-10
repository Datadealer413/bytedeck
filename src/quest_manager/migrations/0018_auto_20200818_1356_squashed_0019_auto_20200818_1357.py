# Generated by Django 2.2.13 on 2020-08-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_manager', '0017_auto_20200815_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questsubmission',
            old_name='game_lab_transfer',
            new_name='do_not_grant_xp',
        ),
        migrations.AlterField(
            model_name='questsubmission',
            name='do_not_grant_xp',
            field=models.BooleanField(default=False, help_text='The student will not earn XP for this quest.'),
        ),
    ]
