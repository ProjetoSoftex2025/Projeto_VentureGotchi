from django.conf import settings
from django.db import models


class Achievement(models.Model):
    """
    Define uma conquista possível no sistema.
    """

    code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Identificador interno (ex: FIRST_MISSION)"
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    xp_bonus = models.PositiveIntegerField(
        default=0,
        help_text="XP extra concedido ao desbloquear a conquista"
    )

    def __str__(self):
        return self.title


class UserAchievement(models.Model):
    """
    Conquista desbloqueada por um usuário.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE
    )

    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "achievement")

    def __str__(self):
        return f"{self.user} - {self.achievement}"