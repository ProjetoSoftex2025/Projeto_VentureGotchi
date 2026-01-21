from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from missions.models import Mission

User = get_user_model()


class IntegrationFlowTests(TestCase):

    def test_full_flow_register_login_mission(self):
        user = User.objects.create_user(
            username="flow",
            password="12345678"
        )

        self.client.login(username="flow", password="12345678")

        mission = Mission.objects.create(
            title="Fluxo Completo",
            xp_reward=100
        )

        response = self.client.get(reverse("core:dashboard"))
        self.assertEqual(response.status_code, 200)
