# Generated by Django 5.0.6 on 2024-06-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_lesson_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.TextField(default='[]'),
        ),
    ]
