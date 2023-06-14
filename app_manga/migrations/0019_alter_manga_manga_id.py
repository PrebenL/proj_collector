# Generated by Django 4.2.2 on 2023-06-14 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_manga', '0018_alter_manga_manga_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='manga_id',
            field=models.CharField(max_length=64, unique=True, validators=[django.core.validators.RegexValidator('^[a-z]*$', 'Only letter characters are allowed.')]),
        ),
    ]