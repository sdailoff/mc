# Generated by Django 4.2.2 on 2023-07-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_schedule_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleag',
            name='hourIni',
        ),
        migrations.AddField(
            model_name='scheduleag',
            name='hourIni',
            field=models.ManyToManyField(to='schedule.hourini'),
        ),
    ]
