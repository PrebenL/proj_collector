# Generated by Django 4.2.2 on 2023-06-14 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_manga', '0011_alter_manga_manga_reading_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chapter',
        ),
        migrations.DeleteModel(
            name='Volume',
        ),
    ]
