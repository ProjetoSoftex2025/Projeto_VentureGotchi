from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import MissionForm
from .models import Mission, MissionProgress
from django.contrib.auth.decorators import permission_required


@login_required
def mission_list_view(request):
    missions = Mission.objects.all()

    # Missões já concluídas pelo usuário
    completed_missions = MissionProgress.objects.filter(
        user=request.user,
        completed=True
    ).values_list("mission_id", flat=True)

    return render(
        request,
        "missions/list.html",
        {
            "missions": missions,
            "completed_missions": completed_missions,
        }
    )


@login_required
def complete_mission_view(request, mission_id):
    mission = get_object_or_404(Mission, id=mission_id)

    progress, created = MissionProgress.objects.get_or_create(
        user=request.user,
        gotchi=request.user.gotchi,
        mission=mission,
    )

    # 🔒 Se já foi concluída, não faz nada
    if progress.completed:
        return redirect("missions:list")

    # Marca como concluída
    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save()  # 👉 aqui dispara a lógica no model

    return redirect("missions:list")

@login_required
@permission_required("missions.add_mission", raise_exception=True)
def create_mission_view(request):
    if request.method == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.professor = request.user  # 🔑 liga ao professor
            mission.save()
            return redirect("core:professor")
    else:
        form = MissionForm()

    return render(request, "missions/create.html", {"form": form})

@login_required
@permission_required("missions.view_missionprogress", raise_exception=True)
def mission_detail_view(request, mission_id):
    mission = get_object_or_404(Mission, id=mission_id, professor=request.user)

    progresses = MissionProgress.objects.filter(
        mission=mission,
        completed=True
    ).select_related("user", "gotchi")

    return render(
        request,
        "missions/detail.html",
        {
            "mission": mission,
            "progresses": progresses
        }
    )

