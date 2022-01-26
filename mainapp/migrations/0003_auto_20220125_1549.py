# Generated by Django 3.2.9 on 2022-01-25 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220117_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='program',
            field=models.ManyToManyField(null=True, to='mainapp.Program', verbose_name='Программа'),
        ),
        migrations.CreateModel(
            name='CommentToStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256, verbose_name='Текст комментария')),
                ('id_stage', models.IntegerField(null=True, verbose_name='Ссылка на пройденный этап')),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='mainapp.candidate', verbose_name='Кандидат')),
            ],
        ),
    ]
