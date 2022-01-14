# Generated by Django 3.2.9 on 2022-01-14 06:12

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdaptationStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=128, verbose_name='Наименование этапа')),
                ('illustration', models.CharField(max_length=256, verbose_name='Ссылка на иллюстрацию')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
                ('point', models.IntegerField(verbose_name='Количество баллов')),
                ('status', models.IntegerField(verbose_name='Статус этапа')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('duration_day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Длительность этапа')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=128, verbose_name='Название награды')),
                ('illustration', models.CharField(max_length=256, verbose_name='Иллюстрация')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
            ],
        ),
        migrations.CreateModel(
            name='AwardCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=128, verbose_name='Название награды')),
                ('id_candidate', models.IntegerField(verbose_name='Кандидат получивший награду')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=64, verbose_name='Отчество')),
                ('mobile_phone', models.CharField(max_length=64, null=True, verbose_name='Телефон')),
                ('email', models.CharField(max_length=64, null=True, verbose_name='Адрес электронной почты')),
                ('post', models.CharField(max_length=64, verbose_name='Должность')),
                ('role', models.CharField(max_length=64, verbose_name='Роль')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
                ('status', models.IntegerField(verbose_name='Статус контакта')),
                ('illustration_link', models.URLField(verbose_name='Ccсылка на иллюстрацию(аватарку)')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=64, verbose_name='Наименование заказчика')),
                ('city', models.CharField(max_length=64, verbose_name='Город')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('status', models.IntegerField(verbose_name='Статус документа')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=128, verbose_name='Наименование документа')),
                ('document_link', models.URLField(verbose_name='Ccылка на файл')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_customer', models.IntegerField(verbose_name='id заказчика')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=64, verbose_name='Отчество')),
                ('post', models.CharField(max_length=64, verbose_name='Должность')),
                ('mobile_phone', models.CharField(max_length=64, verbose_name='Телефон')),
                ('email', models.CharField(max_length=64, verbose_name='Адрес электронной почты')),
                ('status', models.IntegerField(verbose_name='Статус записи')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=128, verbose_name='Наименование цели')),
                ('description', models.CharField(max_length=256, verbose_name='Cодержание цели')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
                ('status', models.IntegerField(verbose_name='Статус цели')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='JobDirectoryCatalogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory', models.CharField(db_index=True, max_length=512, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=128, verbose_name='Наименование уровня')),
                ('illustration', models.CharField(max_length=256, verbose_name='Иллюстрация')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
                ('status', models.IntegerField(verbose_name='Статус уровня')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_license_pack', models.IntegerField(verbose_name='Ссылка на пакет лицезий')),
                ('id_candidate', models.IntegerField(verbose_name='ссылка на кандидата')),
                ('start_date', models.DateField(verbose_name='Дата старта лицензии')),
                ('finish_date', models.DateField(verbose_name='Дата окончания лицензии')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('status', models.IntegerField(verbose_name='Статус лицензии')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='LicensePack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_customer', models.IntegerField(verbose_name='ссылка на кандидата')),
                ('users_count', models.IntegerField(verbose_name='количество приобритенных лицензий')),
                ('users_spent', models.IntegerField(verbose_name='количество потраченных лицензий')),
                ('status', models.IntegerField(verbose_name='Статус лицензии')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.CharField(max_length=512, verbose_name='Текст сообщения')),
                ('id_candidate', models.IntegerField(verbose_name='Кандидат оставивший сообщение')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('viewing_date', models.DateTimeField(verbose_name='Дата просмотра')),
                ('status', models.IntegerField(verbose_name='Статус кандидата')),
            ],
        ),
        migrations.CreateModel(
            name='UserCandidate',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('isCandidate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=128, verbose_name='Наименование программы')),
                ('description', models.CharField(max_length=256, verbose_name='Cодержание программы')),
                ('duration_day', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Длительность адаптации')),
                ('tier', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер по порядку')),
                ('status', models.IntegerField(default=1, verbose_name='Статус программы')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('contact', models.ManyToManyField(blank=True, null=True, to='mainapp.Contact', verbose_name='Контакты')),
                ('customer', models.ManyToManyField(blank=True, null=True, to='mainapp.Customer', verbose_name='Заказчик')),
                ('documents', models.ManyToManyField(blank=True, null=True, to='mainapp.Document', verbose_name='Документы')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='mainapp.employee', verbose_name='Сотрудник создавший запись')),
                ('goals', models.ManyToManyField(blank=True, null=True, to='mainapp.Goal', verbose_name='Цели')),
                ('levels', models.ManyToManyField(blank=True, null=True, to='mainapp.Level', verbose_name='Уровни')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_customer', models.IntegerField(verbose_name='id заказчика')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=64, verbose_name='Отчество')),
                ('post', models.CharField(max_length=64, verbose_name='Должность')),
                ('salary', models.IntegerField(null=True, verbose_name='ЗП')),
                ('mobile_phone', models.CharField(max_length=64, verbose_name='Телефон')),
                ('email', models.CharField(max_length=64, verbose_name='Адрес электронной почты')),
                ('status', models.IntegerField(verbose_name='Статус записи')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('release_date', models.DateField(verbose_name='Дата выходa')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='candidates', to='mainapp.usercandidate', verbose_name='Кандидат')),
                ('program', models.ManyToManyField(to='mainapp.Program', verbose_name='Программа')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=128, verbose_name='Наименование блока')),
                ('description', models.CharField(max_length=256, verbose_name='Cодержание блока')),
                ('tier', models.IntegerField(verbose_name='Номер по порядку')),
                ('status', models.IntegerField(verbose_name='Статус блока')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('id_employee', models.IntegerField(verbose_name='Сотрудник создавший запись')),
                ('adaptationStage', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocks', to='mainapp.adaptationstage', verbose_name='Этап')),
            ],
        ),
        migrations.CreateModel(
            name='AdaptationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_stage', models.IntegerField(null=True, verbose_name='Ссылка на пройденный этап')),
                ('id_goal', models.IntegerField(null=True, verbose_name='Ссылка на выполненную цель')),
                ('point', models.IntegerField(verbose_name='Количество заработанных баллов')),
                ('create_date', models.DateTimeField(verbose_name='Дата создания')),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adaptation_status', to='mainapp.candidate', verbose_name='Кандидат')),
            ],
        ),
        migrations.AddField(
            model_name='adaptationstage',
            name='level',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stages', to='mainapp.level', verbose_name='уровень'),
        ),
    ]
