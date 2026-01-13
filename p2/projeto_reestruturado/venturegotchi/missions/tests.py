from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Mission
from .services.mission_service import complete_mission

from gotchi.models import Gotchi

class MissionFlowTest(TestCase):
    def test_complete_mission_gives_xp(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="tester",
            password="123"
        )

        # 🔥 CRIA GOTCHI EXPLICITAMENTE
        Gotchi.objects.create(user=user, xp=0, level=1)

        mission = Mission.objects.create(
            title="Missão Teste",
            xp_reward=100
        )

        old_xp = user.gotchi.xp

        complete_mission(user, mission)

        user.refresh_from_db()
        self.assertGreater(user.gotchi.xp, old_xp)
