from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    available_seats = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Corso: {self.title}, dal {self.date_start} al {self.date_end}, {self.available_seats} posti"
