from django.contrib import admin
from .models import Achievement, UserAchievement
# comentario

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "xp_bonus")
    search_fields = ("code", "title")


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ("user", "achievement", "unlocked_at")