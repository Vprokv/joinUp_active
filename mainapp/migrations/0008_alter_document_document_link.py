# Generated by Django 3.2.9 on 2022-02-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20220202_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_link',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ccылка на файл'),
        ),
    ]