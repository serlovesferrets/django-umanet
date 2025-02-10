from voti.views import Subject
from .models import Student, SubjectData

Student.objects.all().delete()
SubjectData.objects.all().delete()

student_data: dict[str, list[tuple[Subject, int, int]]] = {
    "Giuseppe Gullo": [
        ("Matematica", 9, 0),
        ("Italiano", 7, 3),
        ("Inglese", 7, 4),
        ("Storia", 7, 4),
        ("Geografia", 5, 7),
    ],
    "Antonio Barbera": [
        ("Matematica", 8, 1),
        ("Italiano", 6, 1),
        ("Inglese", 9, 0),
        ("Storia", 8, 2),
        ("Geografia", 8, 1),
    ],
    "Nicola Spina": [
        ("Matematica", 7, 2),
        ("Italiano", 6, 2),
        ("Inglese", 4, 3),
        ("Storia", 8, 2),
        ("Geografia", 8, 2),
    ],
}

for first_name, last_name in map(lambda n: n.split(), student_data.keys()):
    student = Student(first_name=first_name, last_name=last_name)
    student.save()

for student in Student.objects.all():
    student_name = f"{student.first_name} {student.last_name}"

    for subject_name, grade, leaves in student_data[student_name]:
        student_object = Student.objects.filter(
            first_name=student.first_name,
            last_name=student.last_name,
        ).first()

        if student_object:
            print("student here")
            subject_data = SubjectData(
                name=subject_name,
                grade=grade,
                leaves=leaves,
                student=student_object,
            )

            subject_data.save()
