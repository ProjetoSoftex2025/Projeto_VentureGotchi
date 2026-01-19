from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Progresso, UserProgress


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def criar_progresso_usuario(sender, instance, created, **kwargs):
    if created:
        Progresso.objects.create(usuario=instance)
