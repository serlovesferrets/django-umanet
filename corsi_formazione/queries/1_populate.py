from ..models import Course

from datetime import date

"""
Corso: Programmazione Python, dal 10/03/2025 al 20/03/2025, 30 posti
Corso: Sviluppo Web con Django, dal 15/04/2025 al 30/04/2025, 25 posti
Corso: Intelligenza Artificiale, dal 05/05/2025 al 15/05/2025, 20 posti
Corso: Cybersecurity, dal 20/05/2025 al 30/05/2025, 15 posti
Corso: Database SQL, dal 01/06/2025 al 10/06/2025, 30 posti
"""

courses = [
    Course(
        title="Programmazione Python",
        description="Lorem ipsum dolor sit amen",
        date_start=date(year=2025, month=3, day=10),
        date_end=date(year=2025, month=3, day=20),
        available_seats=30,
    ),
    Course(
        title="Sviluppo Web con Django",
        description="Lorem ipsum dolor sit amen",
        date_start=date(year=2025, month=4, day=15),
        date_end=date(year=2025, month=4, day=30),
        available_seats=25,
    ),
    Course(
        title="Intelligenza Artificiale",
        description="Lorem ipsum dolor sit amen",
        date_start=date(year=2025, month=5, day=5),
        date_end=date(year=2025, month=5, day=15),
        available_seats=20,
    ),
    Course(
        title="Cybersecurity",
        description="Lorem ipsum dolor sit amen",
        date_start=date(year=2025, month=5, day=20),
        date_end=date(year=2025, month=5, day=30),
        available_seats=15,
    ),
    Course(
        title="Database SQL",
        description="Lorem ipsum dolor sit amen",
        date_start=date(year=2025, month=6, day=1),
        date_end=date(year=2025, month=6, day=10),
        available_seats=30,
    ),
]

for course in courses:
    course.save()
