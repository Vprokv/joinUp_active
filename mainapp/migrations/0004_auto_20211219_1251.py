# Generated by Django 3.2.9 on 2021-12-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_adaptationstage_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='id_stage',
        ),
        migrations.AddField(
            model_name='block',
            name='adaptationStage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='mainapp.adaptationstage', verbose_name='Этап'),
        ),
        migrations.AlterField(
            model_name='adaptationstage',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='mainapp.level', verbose_name='уровень'),
        ),
    ]