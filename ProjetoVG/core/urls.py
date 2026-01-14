from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

#app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "dashboard/", views.dashboard, name="dashboard"
    ),  # ligação de url para a página dashboard
    path(
        "progresso/", views.progresso, name="progresso"
    ),  # ligação de url para a página progresso
     path('login/', CustomLoginView.as_view(), name='login'), # ligação de url para a página de login
     path('register/', views.register, name='register'), # ligação de url para a página de cadastro
     path('logout/', LogoutView.as_view(), name='logout'), # ligação de url para a página de logout
     

]
