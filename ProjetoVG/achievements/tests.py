from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Achievement
from .services.achievement_service import unlock_achievement


class AchievementTest(TestCase):
    def test_unlock_achievement(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="player",
            password="123"
        )

        achievement = Achievement.objects.create(
            code="FIRST_TEST",
            title="Primeiro Teste",
            xp_bonus=50
        )

        unlock_achievement(user, achievement)

        self.assertTrue(
            user.userachievement_set.filter(
                achievement=achievement
            ).exists()
        )