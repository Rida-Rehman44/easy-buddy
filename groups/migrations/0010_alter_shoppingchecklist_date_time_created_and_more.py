# Generated by Django 4.2.11 on 2024-05-17 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0009_bulletin_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingchecklist',
            name='date_time_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='shoppingchecklist',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='shoppingchecklist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_shopping_checklists', to=settings.AUTH_USER_MODEL),
        ),
    ]