# Generated by Django 3.1.4 on 2020-12-09 14:59

from django.db import migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_squashed_0010_auto_20201208_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='rtmp_url',
            field=events.models.RTMPURLField(blank=True, null=True),
        ),
    ]
