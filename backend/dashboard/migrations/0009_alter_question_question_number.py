# Generated by Django 5.1.5 on 2025-01-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_question_question_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(unique=True),
        ),
    ]
