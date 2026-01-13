
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@venturegotchi.com",
            password="strongpassword123"
        )

    def test_user_creation(self):
        """Usuário customizado é criado corretamente"""
        self.assertEqual(self.user.email, "test@venturegotchi.com")
        self.assertTrue(self.user.check_password("strongpassword123"))

    def test_login_view(self):
        """Usuário consegue fazer login"""
        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "testuser",
                "password": "strongpassword123"
            }
        )
        self.assertEqual(response.status_code, 302)  # redirect pós login

    def test_profile_requires_login(self):
        """Perfil exige autenticação"""
        response = self.client.get(reverse("accounts:profile"))
        self.assertEqual(response.status_code, 302)

    def test_profile_logged_user(self):
        """Usuário autenticado acessa perfil"""
        self.client.login(username="testuser", password="strongpassword123")
        response = self.client.get(reverse("accounts:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
