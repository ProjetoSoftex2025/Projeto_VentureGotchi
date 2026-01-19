from django.urls import path
from .views import achievement_list_view

app_name = "achievements"

urlpatterns = [
    path("", achievement_list_view, name="list"),
]