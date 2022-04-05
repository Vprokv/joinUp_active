from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User, UserManager


class UserCandidate(User):
    isCandidate = models.BooleanField(default=False)

    objects = UserManager()


class Employee(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_customer = models.IntegerField(verbose_name="id заказчика")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    middle_name = models.CharField(max_length=64, verbose_name="Отчество")
    post = models.CharField(max_length=64, verbose_name="Должность")
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон")
    email = models.CharField(max_length=64, unique=True, verbose_name="Адрес электронной почты")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
    illustration = models.CharField(max_length=256, verbose_name="Иллюстрация", null=True, blank=True)
    password = models.CharField(max_length=256, verbose_name="Пароль")

    def __str__(self):
        return "Сотрудник: {} {}".format(self.last_name, self.first_name)


class Contact(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    middle_name = models.CharField(max_length=64, verbose_name="Отчество")
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон", null=True)
    email = models.CharField(max_length=64, verbose_name="Адрес электронной почты", null=True)
    post = models.CharField(max_length=64, verbose_name="Должность")
    role = models.CharField(max_length=64, verbose_name="Роль")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус контакта")
    illustration_link = models.CharField(max_length=256, verbose_name="Ccсылка на иллюстрацию(аватарку)", null=True, blank=True)
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return "Контакт: {} {}".format(self.last_name, self.first_name)


class Customer(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    customer_name = models.CharField(max_length=64, verbose_name="Наименование заказчика")
    city = models.CharField(max_length=64, verbose_name="Город")
    address = models.CharField(max_length=128, verbose_name="Адрес")
    status = models.IntegerField(verbose_name="Статус документа")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self.customer_name)


class Goal(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    goal_name = models.CharField(max_length=128, verbose_name="Наименование цели")
    description = models.CharField(max_length=256, verbose_name="Cодержание цели")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус цели")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return self.goal_name


class Document(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    document_name = models.CharField(max_length=128, verbose_name="Наименование документа")
    json = models.JSONField(null=True)
    # document_link = models.CharField(max_length=256, verbose_name="Ccылка на файл", null=True, blank=True)
    tier = models.IntegerField(verbose_name="Номер по порядку")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return self.document_name


class Level(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    level_name = models.CharField(max_length=128, verbose_name="Наименование уровня")
    illustration = models.CharField(max_length=256, verbose_name="Иллюстрация", null=True, blank=True)
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус уровня")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return self.level_name


class Program(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    program_name = models.CharField(max_length=128, verbose_name="Наименование программы")
    description = models.CharField(max_length=256, verbose_name="Cодержание программы")
    duration_day = models.IntegerField(
        verbose_name="Длительность адаптации",
        validators=[MinValueValidator(1)],
        default=1
    )
    tier = models.IntegerField(verbose_name="Номер по порядку", validators=[MinValueValidator(1)], default=1)
    status = models.IntegerField(verbose_name="Статус программы", default=1)
    create_date = models.DateTimeField(verbose_name="Дата создания")
    illustration = models.CharField(max_length=256, verbose_name="Иллюстрация", null=True, blank=True)
    employee = models.ForeignKey(
        Employee,
        verbose_name="Сотрудник создавший запись",
        on_delete=models.SET_NULL,
        related_name='programs',
        null=True
    )
    contact = models.ManyToManyField(Contact, verbose_name="Контакты", blank=True)
    customer = models.ManyToManyField(Customer, verbose_name="Заказчик",  blank=True)
    levels = models.ManyToManyField(Level, verbose_name="Уровни", blank=True)
    documents = models.ManyToManyField(Document, verbose_name="Документы", blank=True)
    goals = models.ManyToManyField(Goal, verbose_name="Цели", blank=True)

    def __str__(self):
        return self.program_name


class Candidate(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_customer = models.IntegerField(verbose_name="id заказчика", null=True)
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    middle_name = models.CharField(max_length=64, verbose_name="Отчество")
    post = models.CharField(max_length=64, verbose_name="Должность")
    salary = models.IntegerField(verbose_name="ЗП", null=True)
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон")
    email = models.CharField(max_length=64, verbose_name="Адрес электронной почты")
    status = models.IntegerField(verbose_name="Статус записи", null=True)
    create_date = models.DateTimeField(verbose_name="Дата создания")
    release_date = models.DateField(verbose_name="Дата выходa")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись", null=True)
    illustration = models.CharField(max_length=256, verbose_name="Иллюстрация", null=True, blank=True)
    # candidate = models.ForeignKey(
    #     UserCandidate,
    #     verbose_name="Кандидат",
    #     on_delete=models.SET_NULL,
    #     related_name='candidates',
    #     null=True
    # )
    program = models.ManyToManyField(Program, verbose_name="Программа")

    def __str__(self):
        return "Кандидат: {} {}".format(self.last_name, self.first_name)


class AdaptationStage(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    stage_name = models.CharField(max_length=128, verbose_name="Наименование этапа")
    illustration = models.CharField(max_length=256, verbose_name="Ссылка на иллюстрацию", null=True, blank=True)
    tier = models.IntegerField(verbose_name="Номер по порядку")
    point = models.IntegerField(verbose_name="Количество баллов")
    status = models.IntegerField(verbose_name="Статус этапа")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    duration_day = models.IntegerField(verbose_name="Длительность этапа", validators=[MinValueValidator(1)])
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
    level = models.ForeignKey(
        Level,
        verbose_name="уровень",
        on_delete=models.SET_NULL,
        related_name='stages',
        default=1,
        null=True
    )

    def __str__(self):
        return self.stage_name


class Block(models.Model):
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    # block_name = models.CharField(max_length=128, verbose_name="Наименование блока")
    # description = models.CharField(max_length=256, verbose_name="Cодержание блока")
    # tier = models.IntegerField(verbose_name="Номер по порядку")
    # status = models.IntegerField(verbose_name="Статус блока")
    # create_date = models.DateTimeField(verbose_name="Дата создания")
    # id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
    adaptationStage = models.OneToOneField(
        AdaptationStage,
        verbose_name="Этап",
        on_delete=models.CASCADE,
        primary_key=True
    )
    json = models.JSONField(null=True)

    def __str__(self):
        return self.block_name


class LicensePack(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_customer = models.IntegerField(verbose_name="ссылка на кандидата")
    users_count = models.IntegerField(verbose_name="количество приобритенных лицензий")
    users_spent = models.IntegerField(verbose_name="количество потраченных лицензий")
    status = models.IntegerField(verbose_name="Статус лицензии")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self.id)


class License(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_license_pack = models.IntegerField(verbose_name="Ссылка на пакет лицезий")
    id_candidate = models.IntegerField(verbose_name="ссылка на кандидата")
    start_date = models.DateField(verbose_name="Дата старта лицензии")
    finish_date = models.DateField(verbose_name="Дата окончания лицензии")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    status = models.IntegerField(verbose_name="Статус лицензии")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self.id_license_pack)


class AdaptationStatus(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    candidate = models.ForeignKey(
        Candidate,
        verbose_name="Кандидат",
        on_delete=models.SET_NULL,
        related_name='adaptation_status',
        null=True
    )
    id_stage = models.IntegerField(verbose_name="Ссылка на пройденный этап", null=True)
    id_goal = models.IntegerField(verbose_name="Ссылка на выполненную цель", null=True)
    point = models.IntegerField(verbose_name="Количество заработанных баллов")
    create_date = models.DateTimeField(verbose_name="Дата создания")

    def __str__(self):
        return str(self.id_stage)


class CommentToStage(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        verbose_name="Кандидат",
        on_delete=models.SET_NULL,
        related_name='comment',
        null=True
    )
    comment = models.CharField(max_length=256, verbose_name="Текст комментария")
    id_stage = models.IntegerField(verbose_name="Ссылка на пройденный этап", null=True)

    def __str__(self):
        return str(self.id_stage)


class Award(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    award_name = models.CharField(max_length=128, verbose_name="Название награды")
    illustration = models.CharField(max_length=256, verbose_name="Иллюстрация")
    tier = models.IntegerField(verbose_name="Номер по порядку")

    def __str__(self):
        return str(self.award_name)


class AwardCandidate(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    award_name = models.CharField(max_length=128, verbose_name="Название награды")
    id_candidate = models.IntegerField(verbose_name="Кандидат получивший награду")
    create_date = models.DateTimeField(verbose_name="Дата создания")

    def __str__(self):
        return str(self.award_name)


class Message(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    text_message = models.CharField(max_length=512, verbose_name="Текст сообщения")
    id_candidate = models.IntegerField(verbose_name="Кандидат оставивший сообщение")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    viewing_date = models.DateTimeField(verbose_name="Дата просмотра")
    status = models.IntegerField(verbose_name="Статус кандидата")

    def __str__(self):
        return str(self.id_candidate)


class JobDirectoryCatalogs(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    directory = models.CharField(max_length=512, verbose_name="Должность", db_index=True)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=512, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
