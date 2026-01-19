from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import UserAchievement


@login_required
def achievement_list_view(request):
    """
    Lista conquistas desbloqueadas pelo usuário.
    """

    achievements = UserAchievement.objects.filter(user=request.user)

    return render(
        request,
        "achievements/list.html",
        {"achievements": achievements}
    )