from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Gotchi


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_gotchi_for_user(sender, instance, created, **kwargs):
    """
    Cria automaticamente um Gotchi para cada novo usuário.
    """

    if created:
        Gotchi.objects.create(user=instance)