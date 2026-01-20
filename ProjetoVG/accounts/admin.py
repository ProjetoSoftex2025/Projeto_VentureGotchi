from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.contrib.auth import get_user_model

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin customizado para visualizar os campos extras
    definidos pelo projeto VentureGotchi.
    """

    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
        'get_groups'
    )

    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active")
    

User = get_user_model() 
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'get_groups')
    search_fields = ('username', 'email')

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])

    get_groups.short_description = 'Grupos'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)