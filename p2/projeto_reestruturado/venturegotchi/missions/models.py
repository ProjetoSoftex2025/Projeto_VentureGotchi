from django.conf import settings
from django.db import models


class Mission(models.Model):
    """
    Modelo base de missões e metas.

    Usado para:
    - Missões diárias
    - Metas semanais / mensais
    """

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    MISSION_TYPE_CHOICES = (
        (DAILY, "Diária"),
        (WEEKLY, "Semanal"),
        (MONTHLY, "Mensal"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    mission_type = models.CharField(
        max_length=10,
        choices=MISSION_TYPE_CHOICES,
        default=DAILY
    )

    xp_reward = models.PositiveIntegerField(default=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MissionProgress(models.Model):
    """
    Registra o progresso do usuário em uma missão.
    Mantém histórico e evita missões repetidas infinitamente.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE
    )

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "mission")

    def __str__(self):
        return f"{self.user} - {self.mission}"