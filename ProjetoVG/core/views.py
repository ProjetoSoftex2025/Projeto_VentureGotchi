from core.permissions import usuario_no_grupo
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Progresso
from .forms import CustomUserCreationForm

from gotchi.models import Gotchi


def home(request):
    context = {
        "nome_usuario": "Gotcher",
        "atividades": ["Desafio_01", "Desafio_02", "Desafio_03"],
    }
    return render(request, "home.html", context)


@login_required
def dashboard(request):
    # Garantir que o usuário tem um Gotchi
    gotchi, created = Gotchi.objects.get_or_create(user=request.user)

    # XP mostrado no dashboard = XP atual rumo ao próximo nível (do Gotchi)
    xp = gotchi.xp
    xp_next = gotchi.xp_to_next_level()

    porcentagem = int((xp / xp_next) * 100) if xp_next else 0

    context = {
        "xp": xp,
        "nivel": gotchi.level,
        "proximo": gotchi.level + 1,
        "porcentagem": porcentagem,
        
            # Grupos / Papéis
        "is_aluno": usuario_no_grupo(request.user, "Alunos"),
        "is_professor": usuario_no_grupo(request.user, "Professores"),
        "is_equipe": usuario_no_grupo(request.user, "Equipe"),
        "is_admin": usuario_no_grupo(request.user, "Admins"),
        
    }

    return render(request, "dashboard.html", context)


@login_required
def progresso(request):
    # Mesmo padrão do dashboard, baseado no Gotchi
    gotchi, created = Gotchi.objects.get_or_create(user=request.user)

    xp = gotchi.xp
    xp_next = gotchi.xp_to_next_level()
    porcentagem = int((xp / xp_next) * 100) if xp_next else 0

    context = {
        "xp": xp,
        "xp_next": xp_next,
        "nivel": gotchi.level,
        "proximo": gotchi.level + 1,
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
            return redirect("core:dashboard")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})

