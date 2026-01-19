from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Gotchi


class GotchiModelTest(TestCase):
    def test_gotchi_created_with_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="teste",
            password="123"
        )

        self.assertTrue(
            hasattr(user, "gotchi"),
            "Usuário deveria possuir um Gotchi automaticamente"
        )