from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile_view(request):
    """
    View simples de perfil.
    O dashboard completo será tratado no app dashboard.
    """
    return render(
        request,
        "accounts/profile.html",
        {"user": request.user}
    )