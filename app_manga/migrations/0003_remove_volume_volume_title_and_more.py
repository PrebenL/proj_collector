# Generated by Django 4.2.2 on 2023-06-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_manga', '0002_alter_manga_manga_alternative_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volume',
            name='volume_title',
        ),
        migrations.AlterField(
            model_name='manga',
            name='manga_alternative_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
