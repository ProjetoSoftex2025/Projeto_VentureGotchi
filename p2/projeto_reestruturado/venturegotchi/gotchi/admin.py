from django.contrib import admin
from .models import Gotchi


@admin.register(Gotchi)
class GotchiAdmin(admin.ModelAdmin):
    """
    Visualização administrativa do estado do avatar (Gotchi).
    """

    fields = (
        "user",
        "level",
        "xp",
        "tecnica",
        "criatividade",
        "disciplina",
        "lideranca",
    )

    list_display = (
        "user",
        "level",
        "xp",
        "tecnica",
        "criatividade",
        "disciplina",
        "lideranca",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    list_filter = ("level",)
