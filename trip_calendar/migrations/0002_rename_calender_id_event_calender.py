# Generated by Django 5.0.6 on 2024-05-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='calender_id',
            new_name='calender',
        ),
    ]