# Generated by Django 3.2.9 on 2022-01-03 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_alter_candidate_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='program',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='program',
        ),
        migrations.RemoveField(
            model_name='level',
            name='program',
        ),
        migrations.AddField(
            model_name='candidate',
            name='customer',
            field=models.ManyToManyField(to='mainapp.Program', verbose_name='Программа'),
        ),
        migrations.AddField(
            model_name='program',
            name='documents',
            field=models.ManyToManyField(to='mainapp.Document', verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='program',
            name='goals',
            field=models.ManyToManyField(to='mainapp.Goal', verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='program',
            name='levels',
            field=models.ManyToManyField(to='mainapp.Level', verbose_name='Уровни'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 10, 32, 3, 175004), verbose_name='Дата выходa'),
        ),
    ]
