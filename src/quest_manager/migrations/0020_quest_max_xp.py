# Generated by Django 2.2.24 on 2021-11-17 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_manager', '0019_auto_20210205_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='max_xp',
            field=models.IntegerField(default=-1, help_text='-1 = unlimited'),
        ),
    ]
