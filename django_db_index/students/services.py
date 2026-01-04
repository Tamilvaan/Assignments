from .models import Student

def seed_students(count=50000):
    students = [
        Student(
            name=f"Student{i}",
            email=f"student{i}@gmail.com",
            age=18 + i % 5
        )
        for i in range(1, count + 1)
    ]
    Student.objects.bulk_create(students)
