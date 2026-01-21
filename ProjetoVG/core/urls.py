from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("progresso/", views.progresso, name="progresso"),
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('missions/', include('missions.urls')),
    path("professor/", views.professor_dashboard, name="professor"),
    path("equipe/", views.equipe, name="equipe"),
    path("conquistas/", views.conquistas, name="conquistas"),
    path("tarefas/", views.tarefas, name="tarefas"),

]

