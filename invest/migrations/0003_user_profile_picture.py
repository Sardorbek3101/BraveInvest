# Generated by Django 4.1.6 on 2023-03-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_author_bookauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]