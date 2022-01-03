# Generated by Django 3.2.9 on 2022-01-03 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20220103_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='program',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='program_details',
        ),
        migrations.RemoveField(
            model_name='program',
            name='customer_detail',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 10, 4, 15, 230893), verbose_name='Дата выходa'),
        ),
        migrations.RemoveField(
            model_name='program',
            name='customer',
        ),
        migrations.AddField(
            model_name='program',
            name='customer',
            field=models.ManyToManyField(to='mainapp.Customer', verbose_name='Заказчик'),
        ),
    ]