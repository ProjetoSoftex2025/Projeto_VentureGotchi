from django.contrib import admin
from .models import Progresso, UserProgress, Profile

admin.site.register(Progresso) 
admin.site.register(UserProgress) 
admin.site.register(Profile)