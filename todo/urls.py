from django.urls import path

from todo.views import (
    # index,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("create-task/", TaskCreateView.as_view(), name="task-create"),
]


app_name = "todo"
