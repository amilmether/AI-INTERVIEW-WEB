# Generated by Django 5.1.5 on 2025-02-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interview', '0003_alter_interview_job_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='video_call_path',
        ),
        migrations.AddField(
            model_name='interview',
            name='video_path',
            field=models.FileField(blank=True, null=True, upload_to='video_interview/'),
        ),
    ]
