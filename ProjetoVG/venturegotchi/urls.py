"""
URL configuration for venturegotchi project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Core (home, dashboard, progresso, etc.)
    path('', include(('core.urls', 'core'), namespace='core')),

    # Autenticação padrão do Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Apps do projeto
    path('gotchi/', include('gotchi.urls')),
    path('missions/', include('missions.urls')),
    path('achievements/', include('achievements.urls')),

    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
