# Generated by Django 4.1.6 on 2023-04-19 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0004_investingcourses_mentorship_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investingcourses',
            old_name='video',
            new_name='video_url',
        ),
    ]
