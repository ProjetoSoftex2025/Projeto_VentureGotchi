# missions/urls.py
from django.urls import path
from . import views

app_name = "missions"

urlpatterns = [
    path("", views.missions_list, name="list"),
]
