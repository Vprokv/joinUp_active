# Generated by Django 3.2.9 on 2021-12-18 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211218_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='adaptationstage',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='mainapp.level', verbose_name='программа'),
        ),
    ]
