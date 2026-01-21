from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Achievement
from gotchi.models import Gotchi

User = get_user_model()


class AchievementTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="achiever",
            password="12345678"
        )
        self.gotchi = Gotchi.objects.get(user=self.user)

        self.achievement = Achievement.objects.create(
            name="Primeiro Passo",
            required_level=2
        )

    def test_achievement_unlock_condition(self):
        self.gotchi.level = 2
        self.gotchi.save()

        unlocked = self.achievement.is_unlocked(self.gotchi)
        self.assertTrue(unlocked)
