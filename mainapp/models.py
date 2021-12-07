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
