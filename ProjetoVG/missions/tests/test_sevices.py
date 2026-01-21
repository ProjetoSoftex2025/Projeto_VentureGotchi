from django.test import TestCase
from django.contrib.auth import get_user_model

from gotchi.models import Gotchi
from missions.models import Mission
from missions.services import complete_mission

User = get_user_model()


class CompleteMissionServiceTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="123456"
        )

        self.gotchi = Gotchi.objects.create(
            user=self.user,
            xp=0,
            level=1
        )

        self.mission = Mission.objects.create(
            user=self.user,
            title="Missão Teste",
            xp_reward=120,
            completed=False
        )

    def test_complete_mission_adds_xp_and_levels_up(self):
        complete_mission(self.user, self.mission.id)

        self.gotchi.refresh_from_db()
        self.mission.refresh_from_db()

        self.assertTrue(self.mission.completed)
        self.assertEqual(self.gotchi.xp, 120)
        self.assertEqual(self.gotchi.level, 1)  # 120 XP = nível 1 (regra atual)
