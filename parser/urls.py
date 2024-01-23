from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_parsed_values, name="get_parsed_values"),
]
