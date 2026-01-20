from django.conf import settings
from django.db import models

from gotchi.services.xp_service import add_xp


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

    # ✅ Campos esperados pelos testes (pontuação por atributo)
    tecnica_pontuacao = models.PositiveIntegerField(default=0)
    lideranca_pontuacao = models.PositiveIntegerField(default=0)
    criatividade_pontuacao = models.PositiveIntegerField(default=0)
    disciplina_pontuacao = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MissionProgress(models.Model):
    """
    Registra o progresso do usuário em uma missão.
    Mantém histórico e evita missões repetidas infinitamente.
    """

    # ✅ Preservado do zip, mas agora opcional para permitir create() via gotchi no teste
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # ✅ Novo campo esperado pelos testes
    gotchi = models.ForeignKey(
        "gotchi.Gotchi",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE
    )

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "mission")

    def save(self, *args, **kwargs):
        # Descobre se está completando agora (para não dar recompensa duas vezes)
        was_completed = False
        if self.pk:
            try:
                was_completed = MissionProgress.objects.only("completed").get(pk=self.pk).completed
            except MissionProgress.DoesNotExist:
                was_completed = False

        # Se veio gotchi e não veio user, preenche user automaticamente
        if self.gotchi and not self.user:
            self.user = self.gotchi.user

        super().save(*args, **kwargs)

        # Se completou agora, aplica recompensas no gotchi
        if self.completed and not was_completed and self.gotchi:
            add_xp(self.gotchi, self.mission.xp_reward)

            # Pontos de atributos
            self.gotchi.tecnica += self.mission.tecnica_pontuacao
            self.gotchi.lideranca += self.mission.lideranca_pontuacao
            self.gotchi.criatividade += self.mission.criatividade_pontuacao
            self.gotchi.disciplina += self.mission.disciplina_pontuacao
            self.gotchi.save(update_fields=["tecnica", "lideranca", "criatividade", "disciplina"])

    def __str__(self):
        # Mantém padrão original de string, preferindo user se existir
        if self.user:
            return f"{self.user} - {self.mission}"
        return f"{self.gotchi} - {self.mission}"
