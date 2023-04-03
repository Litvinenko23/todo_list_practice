from django.urls import path

from todo.views import (
    # index,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskListView, TaskUpdateView, TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("create-task/", TaskCreateView.as_view(), name="task-create"),
    path("update-task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("delete-task/<int:pk>delete/", TaskDeleteView.as_view(), name="tag]sk-delete"),
]


app_name = "todo"
