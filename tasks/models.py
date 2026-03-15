from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Priority model
class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Task model
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    deadline = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# SubTask model
class SubTask(models.Model):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=Task.STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title

# Note model
class Note(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.task.title}"