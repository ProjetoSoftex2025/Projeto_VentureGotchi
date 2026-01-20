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

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    level = models.IntegerField(default=1) 
    xp = models.IntegerField(default=0) 
    next_level = models.IntegerField(default=100) 
    def __str__(self): 
        return f"{self.user.username} - Nível {self.level}"
    
class Profile(models.Model): #Classe para armazenar informações adicionais do usuário
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=100, default="default")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username