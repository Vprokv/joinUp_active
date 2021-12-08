from django.db import models


# Create your models here.

class Program(models.Model):
    program_name = models.CharField(max_length=128, verbose_name="Наименование программы")
    description = models.CharField(max_length=256, verbose_name="Cодержание программы")
    duration_day = models.IntegerField(verbose_name="Длительность адаптации")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    id_customer = models.IntegerField(verbose_name="Заказчик")
    status = models.IntegerField(verbose_name="Статус программы")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Level(models.Model):
    level_name = models.CharField(max_length=128, verbose_name="Наименование уровня")
    illustration = models.ImageField(verbose_name="Иллюстрация")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус уровня")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class AdaptationStage(models.Model):
    stage_name = models.CharField(max_length=128, verbose_name="Наименование этапа")
    illustration = models.ImageField(verbose_name="Ссылка на иллюстрацию")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    point = models.IntegerField(verbose_name="Количество баллов")
    status = models.IntegerField(verbose_name="Статус этапа")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Block(models.Model):
    block_name = models.CharField(max_length=128, verbose_name="Наименование блока")
    description = models.CharField(max_length=256, verbose_name="Cодержание блока")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    id_stage = models.IntegerField(verbose_name="Количество баллов")
    status = models.IntegerField(verbose_name="Статус блока")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Goal(models.Model):
    goal_name = models.CharField(max_length=128, verbose_name="Наименование цели")
    description = models.CharField(max_length=256, verbose_name="Cодержание цели")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус цели")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Document(models.Model):
    document_name = models.CharField(max_length=128, verbose_name="Наименование документа")
    document_link = models.URLField(verbose_name="Ccсылка на файл")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус цели")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Contact(models.Model):
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    middle_name = models.CharField(max_length=64, verbose_name="Отчество")
    post = models.CharField(max_length=64, verbose_name="Должность")
    role = models.CharField(max_length=64, verbose_name="Роль")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус контакта")
    illustration_link = models.URLField(verbose_name="Ccсылка на иллюстрацию(аватарку)")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Customer(models.Model):
    customer_name = models.CharField(max_length=64, verbose_name="Наименование заказчика")
    city = models.CharField(max_length=64, verbose_name="Город")
    address = models.CharField(max_length=128, verbose_name="Адрес")
    status = models.IntegerField(verbose_name="Статус документа")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class License(models.Model):
    id_license_pack = models.IntegerField(verbose_name="Ссфлка пакет лицезий")
    id_candidate = models.IntegerField(verbose_name="ссылка на кандидата")
    start_date = models.DateField(verbose_name="Дата старта лицензии")
    finish_date = models.DateField(verbose_name="Дата окончания лицензии")
    status = models.IntegerField(verbose_name="Статус лицензии")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class UserCandidate(models.Model):
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class UserEmployee(models.Model):
    user_name = models.CharField(verbose_name="Логин / телефон (mobile phone)")
    password = models.CharField(verbose_name="Пароль")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Candidate(models.Model):
    id_user_candidate = models.IntegerField(verbose_name="id пользователя")
    id_customer = models.IntegerField(verbose_name="id заказчика")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    middle_name = models.CharField(max_length=64, verbose_name="Отчество")
    post = models.CharField(max_length=64, verbose_name="Должность")
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон")
    email = models.CharField(max_length=64, verbose_name="Адрес электронной почты")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class Employee(models.Model):
    id_user_employee = models.IntegerField(verbose_name="id пользователя")
    id_customer = models.IntegerField(verbose_name="id заказчика")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    middle_name = models.CharField(max_length=64, verbose_name="Отчество")
    post = models.CharField(max_length=64, verbose_name="Должность")
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон")
    email = models.CharField(max_length=64, verbose_name="Адрес электронной почты")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")


class AdaptationStatus(models.Model):
    id_user_employee = models.IntegerField(verbose_name="id пользователя")
    id_stage = models.IntegerField(verbose_name="Ссылка на пройденный этап")
    id_goal = models.IntegerField(verbose_name="Ссылка на выполненную цель")
    point = models.IntegerField(verbose_name="Количество заработанных баллов")
    create_date = models.DateTimeField(verbose_name="Дата создания")


class Award(models.Model):
    award_name = models.CharField(max_length=128, verbose_name="Название награды")
    illustration = models.ImageField(verbose_name="Иллюстрация")
    tier = models.IntegerField(verbose_name="Номер по порядку")


class AwardCandidate(models.Model):
    award_name = models.CharField(max_length=128, verbose_name="Название награды")
    id_candidate = models.IntegerField(verbose_name="Кандидат получивший награду")
    create_date = models.DateTimeField(verbose_name="Дата создания")


class Message(models.Model):
    text_message = models.CharField(max_length=512, verbose_name="Текст сообщения")
    id_candidate = models.IntegerField(verbose_name="Кандидат оставивший сообщение")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    viewing_date = models.DateTimeField(verbose_name="Дата создания")
    status = models.IntegerField(verbose_name="Статус кандидата")