from django.conf import settings
from django.db import models
from django.conf import settings
from django.db import models
class Mission(models.Model):
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="missions_criadas"
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    xp_reward = models.PositiveIntegerField(default=50)

    tecnica_pontuacao = models.PositiveIntegerField(default=0)
    lideranca_pontuacao = models.PositiveIntegerField(default=0)
    criatividade_pontuacao = models.PositiveIntegerField(default=0)
    disciplina_pontuacao = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

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
        # Se completou agora, aplica recompensas no gotchi
        if self.completed and not was_completed and self.gotchi:
            # XP (usa lógica centralizada do Gotchi)
            self.gotchi.add_xp(self.mission.xp_reward)

            # Stats (também centralizados no Gotchi)
            self.gotchi.add_stat("tecnica", self.mission.tecnica_pontuacao)
            self.gotchi.add_stat("lideranca", self.mission.lideranca_pontuacao)
            self.gotchi.add_stat("criatividade", self.mission.criatividade_pontuacao)
            self.gotchi.add_stat("disciplina", self.mission.disciplina_pontuacao)


    def __str__(self):
        # Mantém padrão original de string, preferindo user se existir
        if self.user:
            return f"{self.user} - {self.mission}"
        return f"{self.gotchi} - {self.mission}"
