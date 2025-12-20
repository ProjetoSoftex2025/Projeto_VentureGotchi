from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "dashboard/", views.dashboard, name="dashboard"
    ),  # ligação de url para a página dashboard
    path(
        "progresso/", views.progresso, name="progresso"
    ),  # ligação de url para a página progresso
]
