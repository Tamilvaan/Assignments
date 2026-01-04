from django.core.management.base import BaseCommand
from students.services import seed_students

class Command(BaseCommand):
    help = "Insert dummy students"

    def handle(self, *args, **kwargs):
        seed_students()
        self.stdout.write(self.style.SUCCESS("50,000 students inserted"))
