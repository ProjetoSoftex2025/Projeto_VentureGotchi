from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from .forms import CustomUserCreationForm
from gotchi.models import Gotchi
from django.contrib.auth.decorators import login_required, permission_required
from missions.models import Mission, MissionProgress
from django.db.models import Count, Q

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



def home(request):
    context = {
        "nome_usuario": "Gotcher",
        "atividades": ["Desafio_01", "Desafio_02", "Desafio_03"],
    }
    return render(request, "home.html", context)


@login_required
def dashboard(request):
    gotchi, created = Gotchi.objects.get_or_create(user=request.user)

    xp = gotchi.xp
    xp_next = gotchi.xp_to_next_level()
    porcentagem = int((xp / xp_next) * 100) if xp_next else 0

    context = {
        "nivel": gotchi.level,
        "xp": xp,
        "proximo": gotchi.level + 1,
        "porcentagem": porcentagem,

        # 👇 stats sincronizados com o banco
        **gotchi.stats_dict(),
    }

    return render(request, "dashboard.html", context)


@login_required
def progresso(request):
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
        **gotchi.stats_dict(),
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

@login_required
def equipe(request):
    return render(request, "equipe/equipe.html")


@login_required
def conquistas(request):
    return render(request, "conquistas/conquistas.html")


@login_required
def tarefas(request):
    return render(request, "tarefas/tarefas.html")
