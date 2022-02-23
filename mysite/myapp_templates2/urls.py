from django.urls import path
from . import views

urlpatterns = [
    path("about1/", views.test_templates1, name="test_templates1"),
    path("about2/", views.test_templates2, name="test_templates2")
]

