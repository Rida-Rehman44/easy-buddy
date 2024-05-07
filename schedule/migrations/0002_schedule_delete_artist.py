# Generated by Django 4.2.11 on 2024-05-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Day", models.DateTimeField(max_length=20)),
                ("Stage", models.IntegerField(max_length=10)),
                ("Hours", models.IntegerField(max_length=10)),
                ("genre", models.CharField(max_length=30)),
                ("country", models.CharField(max_length=30)),
                ("firstname", models.CharField(max_length=40)),
                ("lastname", models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name="Artist",
        ),
    ]
