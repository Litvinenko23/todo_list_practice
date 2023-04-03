from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


def index(request):
    tags = Tag.objects.all()

    context = {
        "tags": tags,
    }

    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"


class TaskListView(generic.ListView):
    model = Task
