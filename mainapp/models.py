from django.db import models


# Create your models here.
# TODO: Crete index for adaptation stage table on  levelId.
class Employee(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
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

    def __str__(self):
        return "Сотрудник: {} {}".format(self.last_name, self.first_name)


class Program(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    program_name = models.CharField(max_length=128, verbose_name="Наименование программы")
    description = models.CharField(max_length=256, verbose_name="Cодержание программы")
    duration_day = models.IntegerField(verbose_name="Длительность адаптации")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    id_customer = models.IntegerField(verbose_name="Заказчик")
    status = models.IntegerField(verbose_name="Статус программы")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return self.program_name


class Level(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    level_name = models.CharField(max_length=128, verbose_name="Наименование уровня")
    illustration = models.CharField(max_length=256, verbose_name="Иллюстрация")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус уровня")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
    program = models.ForeignKey(
        Program,
        verbose_name="программа",
        on_delete=models.CASCADE,
        related_name='levels',
        default=1
    )

    def __str__(self):
        return self.level_name


class AdaptationStage(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    stage_name = models.CharField(max_length=128, verbose_name="Наименование этапа")
    illustration = models.CharField(max_length=256, verbose_name="Ссылка на иллюстрацию")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    point = models.IntegerField(verbose_name="Количество баллов")
    status = models.IntegerField(verbose_name="Статус этапа")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
    level = models.ForeignKey(
        Level,
        verbose_name="уровень",
        on_delete=models.CASCADE,
        related_name='stages',
        default=1
    )

    def __str__(self):
        return self.stage_name


class Block(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    block_name = models.CharField(max_length=128, verbose_name="Наименование блока")
    description = models.CharField(max_length=256, verbose_name="Cодержание блока")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    id_stage = models.IntegerField(verbose_name="Этап")
    status = models.IntegerField(verbose_name="Статус блока")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return self.block_name


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
    document_link = models.URLField(verbose_name="Ccсылка на файл")
    tier = models.IntegerField(verbose_name="Номер по порядку")
    status = models.IntegerField(verbose_name="Статус цели")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return self.document_name


class Contact(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
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


class LicensePack(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_customer = models.IntegerField(verbose_name="ссылка на кандидата")
    users_count = models.IntegerField(verbose_name="количество приобритенных лицензий")
    users_spent = models.IntegerField(verbose_name="количество потраченных лицензий")
    status = models.IntegerField(verbose_name="Статус лицензии")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self.id_license_pack)


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


class UserCandidate(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    mobile_phone = models.CharField(max_length=64, verbose_name="Телефон")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self.mobile_phone)


class UserEmployee(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    user_name = models.CharField(max_length=64, verbose_name="Логин / телефон (mobile phone)")
    password = models.CharField(max_length=64, verbose_name="Пароль")
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self.user_name)


class Candidate(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
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

    def __str__(self):
        return "Кандидат: {} {}".format(self.last_name, self.first_name)


class AdaptationStatus(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_user_employee = models.IntegerField(verbose_name="id пользователя")
    id_stage = models.IntegerField(verbose_name="Ссылка на пройденный этап")
    id_goal = models.IntegerField(verbose_name="Ссылка на выполненную цель")
    point = models.IntegerField(verbose_name="Количество заработанных баллов")
    create_date = models.DateTimeField(verbose_name="Дата создания")

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


class LnkLevelProgram(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
    id_level = models.ForeignKey(Level, verbose_name="id level", on_delete=models.CASCADE)
    id_program = models.ForeignKey(Program, verbose_name="id program", on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name="Статус записи")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")

    def __str__(self):
        return str(self)

# class LnkStageLevel(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
#     id_stage = models.ForeignKey(AdaptationStage, verbose_name="id stage", on_delete=models.CASCADE)
#     id_level = models.ForeignKey(Level, verbose_name="id level", on_delete=models.CASCADE)
#     status = models.IntegerField(verbose_name="Статус записи")
#     create_date = models.DateTimeField(verbose_name="Дата создания")
#     id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
#
#     def __str__(self):
#         return str(self)


# class LnkGoalProgram(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
#     id_goal = models.ForeignKey(Goal, verbose_name="id goal", on_delete=models.CASCADE)
#     id_program = models.ForeignKey(Program, verbose_name="id program", on_delete=models.CASCADE)
#     status = models.IntegerField(verbose_name="Статус записи")
#     create_date = models.DateTimeField(verbose_name="Дата создания")
#     id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
#
#     def __str__(self):
#         return str(self)
#
#
# class LnkDocumentProgram(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
#     id_document = models.ForeignKey(Document, verbose_name="id document", on_delete=models.CASCADE)
#     id_program = models.ForeignKey(Program, verbose_name="id program", on_delete=models.CASCADE)
#     status = models.IntegerField(verbose_name="Статус записи")
#     create_date = models.DateTimeField(verbose_name="Дата создания")
#     id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
#
#     def __str__(self):
#         return str(self)
#
#
# class LnkContactProgram(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', db_index=True)
#     id_contact = models.ForeignKey(Contact, verbose_name="id contact", on_delete=models.CASCADE)
#     id_program = models.ForeignKey(Program, verbose_name="id program", on_delete=models.CASCADE)
#     status = models.IntegerField(verbose_name="Статус записи")
#     create_date = models.DateTimeField(verbose_name="Дата создания")
#     id_employee = models.IntegerField(verbose_name="Сотрудник создавший запись")
#
#     def __str__(self):
#         return str(self)
