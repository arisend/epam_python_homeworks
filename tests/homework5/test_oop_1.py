import pytest
from homework_05.hw.oop_1 import Student, Teacher


@pytest.fixture
def student_fix(oop_homework_fix, expired_homework_fix):
    student = Student('Roman', 'Petrov')
    student.first_name  # Petrov
    student.do_homework(oop_homework_fix)
    student.do_homework(expired_homework_fix)  # You are late
    return student


@pytest.fixture
def teacher_fix():
    teacher = Teacher('Daniil', 'Shadrin')
    teacher.last_name  # Daniil
    return teacher


@pytest.fixture
def expired_homework_fix(teacher_fix):
    expired_homework = teacher_fix.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'
    return expired_homework


@pytest.fixture
def oop_homework_fix(teacher_fix):
    # create function from method and use it
    create_homework_too = teacher_fix.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00
    return oop_homework


def test_negative_case(teacher_fix, expired_homework_fix, oop_homework_fix, student_fix):
    """Testing wrong cases"""
    assert str(teacher_fix.last_name) != "Kirill"  # Daniil
    assert str(expired_homework_fix.text) != 'Learn generators'
    assert student_fix.do_homework(expired_homework_fix) != expired_homework_fix


def test_positive_case(teacher_fix, student_fix, expired_homework_fix, oop_homework_fix):
    """Testing correct cases"""
    assert str(student_fix.first_name) == "Petrov"  # Petrov
    assert str(expired_homework_fix.deadline) == "0:00:00"
    assert str(oop_homework_fix.deadline) == "5 days, 0:00:00"
