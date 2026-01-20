from django.conf import settings
from django.db import models
import uuid


class Achievement(models.Model):
    """
    Define uma conquista possível no sistema.
    """

    # ✅ Campos esperados pelos testes
    name = models.CharField(max_length=100, default="", blank=True)
    required_level = models.PositiveIntegerField(default=1)

    # ✅ Campos originais (preservados), com defaults para não quebrar create() do teste
    code = models.CharField(
        max_length=50,
        unique=True,
        default=uuid.uuid4,
        help_text="Identificador interno (ex: FIRST_MISSION)"
    )

    title = models.CharField(max_length=100, default="", blank=True)
    description = models.TextField(blank=True)

    xp_bonus = models.PositiveIntegerField(
        default=0,
        help_text="XP extra concedido ao desbloquear a conquista"
    )

    # ✅ Método exigido pelo teste
    def is_unlocked(self, gotchi) -> bool:
        return getattr(gotchi, "level", 0) >= self.required_level

    def save(self, *args, **kwargs):
        # Compatibilidade: se o teste criar via name, mantém title preenchido
        if not self.title and self.name:
            self.title = self.name
        if not self.name and self.title:
            self.name = self.title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or self.name


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
