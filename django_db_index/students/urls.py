from django.urls import path
from .views import seed_students_view

urlpatterns = [
    path('seed/', seed_students_view),
]
