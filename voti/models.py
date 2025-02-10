from django.db import models


class SubjectData(models.Model):
    name = models.CharField(max_length=15, default="materia")
    grade = models.PositiveIntegerField(default=7)
    leaves = models.PositiveIntegerField(default=0)
    student = models.ForeignKey("Student", models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} for {self.student}: grade[{self.grade}, leaves[{self.leaves}]]"


class Student(models.Model):
    first_name = models.CharField(max_length=15, default="nome")
    last_name = models.CharField(max_length=15, default="cognome")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
