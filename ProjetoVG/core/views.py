from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from .forms import CustomUserCreationForm
from gotchi.models import Gotchi
from missions.models import Mission
from django.db.models import Count, Q


# ==========================
# HOME / LANDING PAGE
# ==========================
def home(request):
    """
    Página inicial / landing do VentureGotchi.
    Apresenta o propósito do projeto.
    """
    return render(request, "home.html", {
        "nome_usuario": "Gotcher"
    })


# ==========================
# DASHBOARD DO ALUNO
# ==========================
@login_required
def dashboard(request):
    gotchi, _ = Gotchi.objects.get_or_create(user=request.user)

    xp = gotchi.xp
    xp_next = gotchi.xp_to_next_level()
    porcentagem = int((xp / xp_next) * 100) if xp_next else 0

    context = {
        "gotchi": gotchi,
        "nivel": gotchi.level,
        "xp": xp,
        "proximo": gotchi.level + 1,
        "porcentagem": porcentagem,
        **gotchi.stats_dict(),
    }

    return render(request, "dashboard.html", context)


# ==========================
# PROGRESSO DO ALUNO
# ==========================
@login_required
def progresso(request):
    gotchi, _ = Gotchi.objects.get_or_create(user=request.user)

    xp = gotchi.xp
    xp_next = gotchi.xp_to_next_level()
    porcentagem = int((xp / xp_next) * 100) if xp_next else 0

    context = {
        "xp": xp,
        "xp_next": xp_next,
        "nivel": gotchi.level,
        "proximo": gotchi.level + 1,
        "porcentagem": porcentagem,
        **gotchi.stats_dict(),
    }

    return render(request, "progresso.html", context)


# ==========================
# DASHBOARD DO PROFESSOR
# ==========================
@login_required
@permission_required("missions.view_mission", raise_exception=True)
def professor_dashboard(request):
    missions = (
        Mission.objects
        .filter(professor=request.user)
        .annotate(
            completed_count=Count(
                "missionprogress",
                filter=Q(missionprogress__completed=True)
            )
        )
    )

    return render(
        request,
        "professor/dashboard.html",
        {"missions": missions}
    )


# ==========================
# AUTENTICAÇÃO
# ==========================
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


# ==========================
# OUTRAS PÁGINAS
# ==========================
@login_required
def equipe(request):
    return render(request, "equipe/equipe.html")


@login_required
def conquistas(request):
    return render(request, "conquistas/conquistas.html")


@login_required
def tarefas(request):
    return render(request, "tarefas/tarefas.html")
