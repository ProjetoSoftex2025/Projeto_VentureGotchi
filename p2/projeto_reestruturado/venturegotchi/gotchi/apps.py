from django.apps import AppConfig


class GotchiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gotchi"

    def ready(self):
        # Importação explícita dos signals para garantir registro
        import gotchi.signals