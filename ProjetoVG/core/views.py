from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Progresso
from .forms import CustomUserCreationForm


def home(request):
    context = {
        "nome_usuario": "Gotcher",
        "atividades": ["Desafio_01", "Desafio_02", "Desafio_03"],
    }
    return render(request, "home.html", context)


@login_required
def dashboard(request):
    progresso, created = Progresso.objects.get_or_create(
        usuario=request.user
    )

    xp = progresso.pontos

    if xp < 100:
        nivel = "Iniciante"
        proximo = "Intermediário"
        porcentagem = xp
    elif xp < 300:
        nivel = "Intermediário"
        proximo = "Avançado"
        porcentagem = int((xp / 300) * 100)
    else:
        nivel = "Avançado"
        proximo = "Máximo"
        porcentagem = 100

    context = {
        "xp": xp,
        "nivel": nivel,
        "proximo": proximo,
        "porcentagem": porcentagem,
    }

    return render(request, "dashboard.html", context)


@login_required
def progresso(request):
    progresso, created = Progresso.objects.get_or_create(
        usuario=request.user
    )

    xp = progresso.pontos

    if xp < 100:
        nivel = "Iniciante"
        proximo = "Intermediário"
        porcentagem = xp
    elif xp < 300:
        nivel = "Intermediário"
        proximo = "Avançado"
        porcentagem = int((xp / 300) * 100)
    else:
        nivel = "Avançado"
        proximo = "Máximo"
        porcentagem = 100

    context = {
        "xp": xp,
        "nivel": nivel,
        "proximo": proximo,
        "porcentagem": porcentagem,
    }

    return render(request, "progresso.html", context)


class CustomLoginView(LoginView):
    template_name = "login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})
