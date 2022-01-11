from django.db import models

import datetime


# Create your models here.
class NotAHomeworkException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotATeacherException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotAStudentException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DeadlineError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


#
class Student(Person):
    """Атрибуты:
    last_name
    first_name
    Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None"""

    def do_homework(self, Homework, text):
        if not Homework.is_active():
            raise DeadlineError('You are late')
        else:
            HWresult = Homework.homeworkresult_set.create(author=f"{self.first_name} {self.last_name}", solution=text,
                                                          created=datetime.datetime.now())
            return HWresult


#
class Teacher(Person):
    """Атрибуты:
    last_name
    first_name
    Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект."""

    #
    def check_homework(self, HomeworkResult):
        if len(HomeworkResult.solution) > 5:
            HomeworkResult.done = True
            HomeworkResult.cheaked = True
            HomeworkResult.created = datetime.datetime.now()
            HomeworkResult.save()
            return True
        else:
            return False

    @staticmethod
    def reset_results():
        HomeworkResult.objects.all().delete()

    def create_homework(self, text, days):
        return Homework(teacher=f"{self.first_name} {self.last_name}", text=text,
                        deadline=datetime.timedelta(days=days), created=datetime.datetime.now())


#
class Homework(models.Model):
    """Homework принимает на вход 2 атрибута: текст задания и количество дней на это задание
    Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством дней на выполнение
    created - c точной датой и временем создания
    Методы:
    is_active - проверяет не истекло ли время на выполнение задания, возвращает boolean"""
    teacher = models.CharField(max_length=60)
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField()

    def is_active(self):
        return self.created + self.deadline > datetime.datetime.now()


#

class HomeworkResult(models.Model):
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE)
    author = models.CharField(max_length=60, default=None)
    solution = models.TextField(default=None)
    created = models.DateTimeField()
    done = models.BooleanField(default=False)
    cheaked = models.BooleanField(default=False)

    def __str__(self):
        return f"at:{self.author}, cr:{self.created}, done:{self.done}"
