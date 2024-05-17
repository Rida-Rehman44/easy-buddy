# Generated by Django 4.2.11 on 2024-05-12 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_alter_bulletinboardmessage_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinboardmessage',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_bulletinboard_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]