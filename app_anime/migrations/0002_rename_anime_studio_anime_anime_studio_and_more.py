# Generated by Django 4.2.2 on 2023-06-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_anime', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='anime_Studio',
            new_name='anime_studio',
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_watching_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Watching', 'Watching'), ('Dropped', 'Dropped'), ('On_hold', 'On Hold'), ('Planning_To_Watch', 'Planning To Watch')], default='reading', max_length=250),
        ),
    ]
