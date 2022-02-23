from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shownow/", views.show_datetime, name="show_datetime")
]


