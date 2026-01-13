from django.contrib import admin
from .models import Mission, MissionProgress


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("title", "mission_type", "xp_reward")
    list_filter = ("mission_type",)
    search_fields = ("title",)


@admin.register(MissionProgress)
class MissionProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "mission", "completed", "completed_at")
    list_filter = ("completed",)