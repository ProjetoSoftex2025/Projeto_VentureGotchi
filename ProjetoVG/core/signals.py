from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import User 
from .models import Progresso, UserProgress
# Signal responsável por criar automaticamente o Progresso sempre que um novo usuário é criado no sistema.
# Evita erros e garante consistência dos dados.

@receiver(post_save, sender=User)

def criar_progresso_usuario(sender, instance, created, **kwargs): 
    if created:
        Progresso.objects.create(usuario=instance) 
    else: 
        # garante consistência se você mudar a lógica de salvamento do usuário
        progresso = getattr(instance, "progresso", None) 
        if progresso and hasattr(progresso, "atualizar_nivel_e_meta"):
            progresso.atualizar_nivel_e_meta()
            