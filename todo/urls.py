from django.urls import path

from todo.views import index


urlpatterns = [
    path("", index, name="index"),
    # path("tags/", index, name="index")
]


app_name = "todo"
