from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Gotchi

User = get_user_model()


class GotchiTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="player",
            password="12345678"
        )
        self.gotchi = Gotchi.objects.get(user=self.user)

    def test_gotchi_created_automatically(self):
        self.assertIsNotNone(self.gotchi)
        self.assertEqual(self.gotchi.level, 1)

    def test_gain_xp_and_level_up(self):
        self.gotchi.add_xp(200)
        self.gotchi.refresh_from_db()

        self.assertGreater(self.gotchi.level, 1)
        self.assertGreaterEqual(self.gotchi.xp, 0)
