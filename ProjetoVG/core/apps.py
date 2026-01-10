from django.apps import AppConfig

# Configuração principal do app Core, responsável pelo registro do aplicativo e definição de comportamentos padrão dentro do projeto Django.
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
