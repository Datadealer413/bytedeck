# Generated by Django 2.0.9 on 2019-01-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_manager', '0002_auto_20190101_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='instructions',
            field=models.TextField(blank=True, verbose_name='Quest Details'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='submission_details',
            field=models.TextField(blank=True, verbose_name='Submission Instructions'),
        ),
    ]
