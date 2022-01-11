import os
import sys
import django
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


dbs = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': r'C:\Users\Alexey\Documents\GitHub\epam_python_homeworks\homework_12_django\main.db',
    }
}

from django.conf import settings



settings.configure(
    DATABASES=dbs,
    INSTALLED_APPS=('School.apps.SchoolConfig',))  # add all the apps you need here
django.setup()

from School.models import *


def test_report():
    result = []
    for hwr in HomeworkResult.objects.filter(done=True).select_related('homework_id'):
        result.append([hwr.author, hwr.homework_id.created, hwr.homework_id.teacher])
    return result


fields = ['Student', 'Creation date', 'Teacher']

with open('report.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(test_report())

def old_sequence_from_task_6():
    opp_teacher = Teacher(first_name='Daniil', last_name='Shadrin')
    advanced_python_teacher = Teacher(first_name='Aleksandr', last_name='Smetanin')
    opp_teacher.save()
    advanced_python_teacher.save()

    lazy_student = Student(first_name='Roman', last_name='Petrov')
    good_student = Student(first_name='Lev', last_name='Sokolov')
    lazy_student.save()
    good_student.save()

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)
    oop_hw.save()
    docs_hw.save()
#
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_1.save()
#
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_2.save()
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    result_3.save()
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
        result_4.save()
    except Exception:
        print('There was an exception here')
#
#
    advanced_python_teacher.check_homework(result_1)


    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(HomeworkResult.objects.all())
    Teacher.reset_results()
    print(HomeworkResult.objects.all())


