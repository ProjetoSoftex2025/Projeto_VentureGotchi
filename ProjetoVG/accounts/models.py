from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User Model exigido pelo projeto VentureGotchi.

    Estende o AbstractUser padrão do Django para suportar:
    - bio profissional
    - interesses
    - avatar inicial
    """

    bio = models.TextField(
        blank=True,
        help_text="Breve descrição profissional do usuário"
    )

    interests = models.CharField(
        max_length=255,
        blank=True,
        help_text="Interesses separados por vírgula (ex: Python, UX, Negócios)"
    )

    avatar = models.CharField(
        max_length=100,
        default="default.png",
        help_text="Nome do arquivo do avatar inicial"
    )

    def __str__(self):
        return self.username
