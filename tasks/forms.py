from django import forms
from .models import Task, SubTask, Category, Priority, Note

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline', 'category', 'priority']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['parent_task', 'title', 'status']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['task', 'content']