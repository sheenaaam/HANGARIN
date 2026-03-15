from django.urls import path
from .views import (
    DashboardView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),

    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),

    path("subtasks/", SubTaskListView.as_view(), name="subtask_list"),
    path("subtasks/create/", SubTaskCreateView.as_view(), name="subtask_create"),
    path("subtasks/update/<int:pk>/", SubTaskUpdateView.as_view(), name="subtask_update"),
    path("subtasks/delete/<int:pk>/", SubTaskDeleteView.as_view(), name="subtask_delete"),

    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/update/<int:pk>/", CategoryUpdateView.as_view(), name="category_update"),
    path("categories/delete/<int:pk>/", CategoryDeleteView.as_view(), name="category_delete"),

    path("priorities/", PriorityListView.as_view(), name="priority_list"),
    path("priorities/create/", PriorityCreateView.as_view(), name="priority_create"),
    path("priorities/update/<int:pk>/", PriorityUpdateView.as_view(), name="priority_update"),
    path("priorities/delete/<int:pk>/", PriorityDeleteView.as_view(), name="priority_delete"),

    path("notes/", NoteListView.as_view(), name="note_list"),
    path("notes/create/", NoteCreateView.as_view(), name="note_create"),
    path("notes/update/<int:pk>/", NoteUpdateView.as_view(), name="note_update"),
    path("notes/delete/<int:pk>/", NoteDeleteView.as_view(), name="note_delete"),
]