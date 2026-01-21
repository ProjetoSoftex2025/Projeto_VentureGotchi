
# missions/views.py
from django.shortcuts import render

def missions_list(request):
    return render(request, "missions/list.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Mission
from .services.mission_service import complete_mission


@login_required
def mission_list_view(request):
    """
    Lista missões disponíveis.
    """
    missions = Mission.objects.all()
    return render(
        request,
        "missions/list.html",
        {"missions": missions}
    )


@login_required
def complete_mission_view(request, mission_id):
    """
    Endpoint simples para concluir missão.
    """
    mission = get_object_or_404(Mission, id=mission_id)
    complete_mission(request.user, mission)
    return redirect("missions:list")
