# Generated by Django 4.2.2 on 2023-06-13 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_title', models.CharField(max_length=200)),
                ('chapter_number', models.IntegerField(default=1)),
                ('chapter_pages', models.IntegerField(default=1)),
                ('chapter_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga_title', models.CharField(max_length=200)),
                ('manga_alternative_title', models.CharField(max_length=200)),
                ('manga_volumes', models.IntegerField(default=0)),
                ('manga_publisher', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manhwa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manhwa_title', models.CharField(max_length=200)),
                ('manhwa_alternative_title', models.CharField(max_length=200)),
                ('manhwa_volumes', models.IntegerField(default=0)),
                ('manhwa_publisher', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_title', models.CharField(max_length=200)),
                ('volume_number', models.IntegerField(default=0)),
                ('volume_chapters', models.IntegerField(default=1)),
                ('volume_pages', models.IntegerField(default=1)),
                ('volume_read', models.BooleanField(default=False)),
                ('volume_manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_manga.manga')),
            ],
        ),
    ]
