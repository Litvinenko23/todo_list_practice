from django.shortcuts import render

from todo.models import Tag


def index(request):
    tags = Tag.objects.all()

    context = {
        "tags": tags,
    }

    return render(request, "todo/index.html", context=context)
