from typing import Literal
from django.http import HttpRequest
from django.shortcuts import render
from .models import Student, SubjectData

type Subject = (
    Literal["Matematica"]
    | Literal["Italiano"]
    | Literal["Inglese"]
    | Literal["Storia"]
    | Literal["Geografia"]
)

all_subjects: set[Subject] = {
    "Matematica",
    "Italiano",
    "Inglese",
    "Storia",
    "Geografia",
}


def subjects_list(request: HttpRequest):
    context = {"subjects": all_subjects}
    return render(request, "vista_1.html", context)


def get_students_data():
    students = []
    for student in Student.objects.all():
        students.append({
            "name": f"{student.first_name} {student.last_name}",
            "subject_data": SubjectData.objects.filter(
                student__first_name=student.first_name,
                student__last_name=student.last_name,
            ),
        })

    return {"students": students}


def student_grades(request: HttpRequest):
    return render(request, "vista_2.html", context=get_students_data())


def student_averages(request: HttpRequest):
    students_data = get_students_data()
    averages = []

    for student in students_data["students"]:
        sum = 0
        count = 0

        for subject in student["subject_data"]:
            count += 1
            sum += subject.grade

        averages.append({
            "student": student["name"],
            "average": sum / count,
        })

    return render(request, "vista_3.html", context={"averages": averages})


def max_and_min_grades(request: HttpRequest):
    students_data = get_students_data()

    max_grade_data = {"name": "no one", "grade": -1, "subject": "none"}
    min_grade_data = {"name": "no one", "grade": 11, "subject": "none"}

    for student in students_data["students"]:
        for subject in student["subject_data"]:
            if subject.grade > max_grade_data["grade"]:
                max_grade_data["grade"] = subject.grade
                max_grade_data["name"] = student["name"]
                max_grade_data["subject"] = subject.name

            if subject.grade < min_grade_data["grade"]:
                min_grade_data["grade"] = subject.grade
                min_grade_data["name"] = student["name"]
                min_grade_data["subject"] = subject.name

    context = {
        "max_grade_data": max_grade_data,
        "min_grade_data": min_grade_data,
    }

    return render(request, "vista_4.html", context=context)
