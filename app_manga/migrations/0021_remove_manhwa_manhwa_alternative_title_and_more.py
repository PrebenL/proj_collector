# Generated by Django 4.2.2 on 2023-06-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_manga', '0020_alter_manga_manga_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manhwa',
            name='manhwa_alternative_title',
        ),
        migrations.RemoveField(
            model_name='manhwa',
            name='manhwa_publisher',
        ),
        migrations.RemoveField(
            model_name='manhwa',
            name='manhwa_volumes',
        ),
        migrations.AddField(
            model_name='manhwa',
            name='manhwa_chapters',
            field=models.IntegerField(default=0),
        ),
    ]