# Generated by Django 4.2.2 on 2023-06-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_anime', '0002_rename_anime_studio_anime_anime_studio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='anime_watched_episodes',
            field=models.IntegerField(default=0),
        ),
    ]
