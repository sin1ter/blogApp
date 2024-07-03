# Generated by Django 4.2.11 on 2024-04-26 04:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_websitemeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=None, default=None, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]