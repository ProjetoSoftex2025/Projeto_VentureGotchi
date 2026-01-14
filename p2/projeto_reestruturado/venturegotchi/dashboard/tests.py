from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class DashboardViewTest(TestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard:index"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_loads(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="dash",
            password="123"
        )

        self.client.login(username="dash", password="123")
        response = self.client.get(reverse("dashboard:index"))

        self.assertEqual(response.status_code, 200)