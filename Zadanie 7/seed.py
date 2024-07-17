from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import datetime
from my_models import Base, Student, Group, Lecturer, Subject, Grade

DATABASE_URL = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Tworzenie grup
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Tworzenie wykładowców
lecturers = [Lecturer(fullname=fake.name()) for _ in range(5)]
session.add_all(lecturers)
session.commit()

# Tworzenie przedmiotów
subjects = [Subject(name=fake.word(), lecturer=random.choice(lecturers)) for _ in range(8)]
session.add_all(subjects)
session.commit()

# Tworzenie studentów
students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Tworzenie ocen
for student in students:
    for subject in subjects:
        grades = [Grade(student=student, subject=subject, grade=random.uniform(2.0, 5.0), date_received=fake.date_this_year()) for _ in range(20)]
        session.add_all(grades)
session.commit()
