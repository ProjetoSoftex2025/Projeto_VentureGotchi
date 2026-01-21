from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AccountTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="teste",
            email="teste@email.com",
            password="12345678"
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(self.user.check_password("12345678"))

    def test_login(self):
        login = self.client.login(
            username="teste",
            password="12345678"
        )
        self.assertTrue(login)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("core:dashboard"))
        self.assertEqual(response.status_code, 302)  # redirect para login
