from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from missions.models import Mission, MissionProgress
from achievements.models import UserAchievement
from gotchi.models import Gotchi


@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, "dashboard/index.html")


@login_required(login_url="/accounts/login/")
def dashboard_view(request):
    """
    Dashboard central do VentureGotchi.

    Responsável apenas por:
    - agregar dados
    - enviar contexto para o template
    """

    # --- GOTCHI (defensivo, não quebra dashboard) ---
    gotchi, _ = Gotchi.objects.get_or_create(user=request.user)

    # --- MISSÕES ---
    missions = Mission.objects.all()[:5]
    completed_missions = MissionProgress.objects.filter(
        user=request.user,
        completed=True
    ).count()

    # --- CONQUISTAS ---
    achievements = UserAchievement.objects.filter(
        user=request.user
    ).order_by("-unlocked_at")[:5]

    # --- XP REAL (backend) ---
    current_xp = gotchi.xp
    xp_to_next_level = gotchi.xp_to_next_level()

    xp_percent = 0
    if xp_to_next_level > 0:
        xp_percent = min((current_xp / xp_to_next_level) * 100, 100)

    context = {
        "gotchi": gotchi,
        "missions": missions,
        "completed_missions": completed_missions,
        "achievements": achievements,
        "current_xp": current_xp,
        "xp_to_next_level": xp_to_next_level,
        "xp_percent": xp_percent,
    }

    return render(
        request,
        "dashboard/index.html",
        context
    )
