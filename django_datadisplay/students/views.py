from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    context={
        'student':students
    }
    return render(request, 'student_list.html',context)
