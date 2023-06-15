# Generated by Django 4.2.2 on 2023-06-15 18:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_id', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator('^[a-z]*$', 'Only letter characters are allowed.')])),
                ('anime_title', models.CharField(max_length=200)),
                ('anime_alternative_title', models.CharField(blank=True, max_length=100)),
                ('anime_Studio', models.CharField(max_length=200)),
                ('anime_seasons', models.IntegerField(default=0)),
                ('anime_episodes', models.IntegerField(default=0)),
                ('anime_watched_episodes', models.CharField(max_length=200)),
                ('anime_status', models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Unknown', 'Unknown')], default='unknown', max_length=250)),
                ('anime_watching_status', models.CharField(choices=[('Completed', 'Completed'), ('Watching', 'Reading'), ('Dropped', 'Dropped'), ('On_hold', 'On Hold'), ('Planning_To_Watch', 'Planning To Watch')], default='reading', max_length=250)),
                ('anime_cover_image', models.URLField()),
            ],
        ),
    ]
