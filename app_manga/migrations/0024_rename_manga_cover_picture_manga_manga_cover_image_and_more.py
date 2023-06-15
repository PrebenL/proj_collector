# Generated by Django 4.2.2 on 2023-06-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_manga', '0023_manhwa_manhwa_reading_status_manhwa_manhwa_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='manga_cover_picture',
            new_name='manga_cover_image',
        ),
        migrations.AddField(
            model_name='manhwa',
            name='manhwa_cover_image',
            field=models.URLField(default='https://todo.com/image.png'),
            preserve_default=False,
        ),
    ]
