from django.conf import settings
from django.db import models


class Gotchi(models.Model):
    """
    Modelo central do avatar (Gotchi).
    Cada usuário possui exatamente UM Gotchi.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="gotchi"
    )

    # Progressão básica
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=0)

    # Estatísticas base
    tecnica = models.PositiveIntegerField(default=1)
    criatividade = models.PositiveIntegerField(default=1)
    disciplina = models.PositiveIntegerField(default=1)
    lideranca = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    # ---------- LÓGICA DE PROGRESSÃO ----------

    def xp_to_next_level(self) -> int:
        """XP necessária para subir de nível."""
        return self.level * 100

    def level_up(self) -> None:
        """Evolução automática de stats ao subir de nível."""
        self.tecnica += 1
        self.criatividade += 1
        self.disciplina += 1
        self.lideranca += 1

    def add_xp(self, amount: int) -> None:
        """Adiciona XP e gerencia level up automaticamente."""
        self.xp += amount

        while self.xp >= self.xp_to_next_level():
            self.xp -= self.xp_to_next_level()
            self.level += 1
            self.level_up()

        self.save()

    def add_stat(self, stat: str, amount: int = 1) -> None:
        """Incrementa um stat específico."""
        if hasattr(self, stat):
            setattr(self, stat, getattr(self, stat) + amount)
            self.save()

    def stats_dict(self) -> dict:
        """Retorna stats prontos para o template."""
        return {
            "tecnica": self.tecnica,
            "criatividade": self.criatividade,
            "disciplina": self.disciplina,
            "lideranca": self.lideranca,
        }

    def __str__(self):
        return f"Gotchi de {self.user}"

def avatar_image(self) -> str:
    """
    Retorna o caminho do avatar conforme o nível do Gotchi.
    """
    if self.level <= 2:
        return "avatars/Gotchi_Iniciante.png"
    elif self.level <= 10:
        return "avatars/Gotchi_Intermediario.png"
    else:
        return "avatars/Gotchi_Avancado.png"