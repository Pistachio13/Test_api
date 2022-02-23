from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_templates, name="my_templates")
]

