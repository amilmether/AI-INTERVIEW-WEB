# Generated by Django 5.1.5 on 2025-02-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplyPage', '0002_candidate_delete_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='overall_score',
            field=models.IntegerField(null=True),
        ),
    ]
