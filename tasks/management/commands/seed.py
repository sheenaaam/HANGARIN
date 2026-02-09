from django.core.management.base import BaseCommand
from tasks.models import Task, SubTask, Note, Category, Priority
from faker import Faker
from django.utils import timezone
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with fake Tasks, SubTasks, and Notes"

    def handle(self, *args, **kwargs):
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(self.style.ERROR("Please add Categories and Priorities first!"))
            return

        for _ in range(10):  # create 10 tasks
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=random.choice(["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(priorities),
                category=random.choice(categories)
            )
            # SubTasks
            for _ in range(random.randint(1, 3)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4),
                    status=random.choice(["Pending", "In Progress", "Completed"]),
                    parent_task=task
                )
            # Notes
            for _ in range(random.randint(1, 2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )

        self.stdout.write(self.style.SUCCESS("Fake data created successfully!"))
