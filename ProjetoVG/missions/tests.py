from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Mission, MissionProgress
from gotchi.models import Gotchi

User = get_user_model()


class MissionTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="mission_user",
            password="12345678"
        )
        self.gotchi = Gotchi.objects.get(user=self.user)

        self.mission = Mission.objects.create(
            title="Missão Teste",
            xp_reward=50,
            tecnica_pontuacao=2,
            lideranca_pontuacao=1,
            criatividade_pontuacao=1,
            disciplina_pontuacao=2
        )

    def test_complete_mission_gives_xp(self):
        progress = MissionProgress.objects.create(
            mission=self.mission,
            gotchi=self.gotchi,
            completed=True
        )

        self.gotchi.refresh_from_db()

        self.assertGreaterEqual(self.gotchi.xp, 50)

    def test_mission_progress_created(self):
        progress = MissionProgress.objects.create(
            mission=self.mission,
            gotchi=self.gotchi
        )
        self.assertFalse(progress.completed)
