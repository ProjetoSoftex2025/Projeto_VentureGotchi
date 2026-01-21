from django.conf import settings
from django.db import models


class Gotchi(models.Model):
    """
    Modelo central do avatar (Gotchi).

    Cada usuário possui exatamente UM Gotchi.
    Toda a evolução, XP e estatísticas partem deste modelo.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="gotchi"
    )

    # Progressão básica
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=0)

    # Estatísticas base (MVP)
    tecnica = models.PositiveIntegerField(default=1)
    criatividade = models.PositiveIntegerField(default=1)
    disciplina = models.PositiveIntegerField(default=1)
    lideranca = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    # ---------- LÓGICA DE PROGRESSÃO ----------

    def xp_to_next_level(self) -> int:
        """
        XP necessária para subir de nível.
        Curva simples e previsível (MVP).
        """
        return self.level * 100

    def add_xp(self, amount: int) -> None:
        """
        Adiciona XP e gerencia level up automaticamente.
        """
        self.xp += amount

        while self.xp >= self.xp_to_next_level():
            self.xp -= self.xp_to_next_level()
            self.level += 1

        self.save()

    def __str__(self):
        return f"Gotchi de {self.user}"
