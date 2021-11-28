import os
import sys
import pytest
import datetime
from homework_05.hw.oop_1 import Homework, Student, Teacher

teacher = Teacher('Daniil', 'Shadrin')
student = Student('Roman', 'Petrov')
teacher.last_name  # Daniil
student.first_name  # Petrov

expired_homework = teacher.create_homework('Learn functions', 0)
expired_homework.created  # Example: 2019-05-26 16:44:30.688762
expired_homework.deadline  # 0:00:00
expired_homework.text  # 'Learn functions'

# create function from method and use it
create_homework_too = teacher.create_homework
oop_homework = create_homework_too('create 2 simple classes', 5)
oop_homework.deadline  # 5 days, 0:00:00

student.do_homework(oop_homework)
student.do_homework(expired_homework)  # You are late


def test_negative_case():
    """Testing wrong cases"""
    assert str(teacher.last_name) != "Kirill"  # Daniil
    assert str(expired_homework.text) != 'Learn generators'
    assert student.do_homework(expired_homework) != expired_homework


def test_positive_case():
    """Testing correct cases"""
    assert str(student.first_name) == "Petrov"  # Petrov
    assert str(expired_homework.deadline) == "0:00:00"
    assert str(oop_homework.deadline) == "5 days, 0:00:00"
