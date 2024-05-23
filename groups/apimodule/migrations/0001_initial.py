# Generated by Django 5.0.6 on 2024-05-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hunde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rasse', models.CharField(max_length=100)),
                ('alter', models.IntegerField()),
                ('geschlecht', models.CharField(max_length=100)),
                ('bild', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('beschreibung', models.TextField()),
                ('erstellt_am', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
