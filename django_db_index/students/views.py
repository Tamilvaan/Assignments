from django.http import HttpResponse
from .services import seed_students

def seed_students_view(request):
    seed_students(1000)
    return HttpResponse("Students inserted successfully")

