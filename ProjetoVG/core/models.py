from django.db import models
from django.contrib.auth.models import User


class Progresso(models.Model):
    NIVEL_CHOICES = [
        ("Iniciante", "Iniciante"),
        ("Intermediário", "Intermediário"),
        ("Avançado", "Avançado"),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pontos = models.IntegerField(default=0)
    posicao = models.IntegerField(default=0)
    nivel = models.CharField(max_length=50, choices=NIVEL_CHOICES, default="Iniciante")
