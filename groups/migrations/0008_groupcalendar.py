# Generated by Django 4.2.11 on 2024-05-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_user_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calendar_id', models.CharField(max_length=100)),
            ],
        ),
    ]