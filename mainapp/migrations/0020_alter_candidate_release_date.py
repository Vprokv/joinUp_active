# Generated by Django 3.2.9 on 2022-01-03 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20220103_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 10, 5, 44, 462651), verbose_name='Дата выходa'),
        ),
    ]