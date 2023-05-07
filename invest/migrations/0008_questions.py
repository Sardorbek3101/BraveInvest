# Generated by Django 4.1.6 on 2023-05-07 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0007_book_my_favorite_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Any questions about our service', 'Any questions about our service?'), ('Any recommendations about courses', 'Any recommendations about courses?'), ('Any issues?', 'Any issues'), ('Support us..', 'Support us')], default='Any questions about our service', max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
