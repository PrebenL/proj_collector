# Generated by Django 4.2.2 on 2023-06-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_manga', '0006_alter_manga_manga_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='manga_author',
            field=models.CharField(default='masashi kishimoto', max_length=200),
        ),
        migrations.AddField(
            model_name='manga',
            name='manga_read_volumes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='manga',
            name='manga_reading_status',
            field=models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('unknown', 'Unknown')], default='reading', max_length=250),
        ),
        migrations.AlterField(
            model_name='manga',
            name='manga_status',
            field=models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('unknown', 'Unknown')], default='unknown', max_length=250),
        ),
    ]
