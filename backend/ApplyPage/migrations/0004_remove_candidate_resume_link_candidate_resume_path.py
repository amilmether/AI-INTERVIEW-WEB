# Generated by Django 5.1.5 on 2025-02-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplyPage', '0003_candidate_overall_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='resume_link',
        ),
        migrations.AddField(
            model_name='candidate',
            name='resume_path',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
