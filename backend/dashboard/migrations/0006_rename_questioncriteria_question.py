# Generated by Django 5.1.5 on 2025-01-27 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionCriteria',
            new_name='Question',
        ),
    ]
