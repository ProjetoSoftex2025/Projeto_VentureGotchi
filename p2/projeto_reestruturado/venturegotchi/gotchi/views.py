from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def gotchi_status_view(request):
    """
    View simples de leitura do estado do Gotchi.
    O layout HUD será responsabilidade do app dashboard.
    """

    return render(
        request,
        "gotchi/status.html",
        {"gotchi": request.user.gotchi}
    )