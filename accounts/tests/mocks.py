from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.models import User


class Mocks(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.rota_register = "/api/accounts/"
        cls.rota_login = "/api/login/"
        cls.seller = {
            "username": "alisson",
            "password": "1234",
            "first_name": "alisson",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.seller_2 = {
            "username": "alexia",
            "password": "1234",
            "first_name": "alexia",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.instance_seller = User.objects.create_user(**cls.seller_2)
        cls.token_seller = Token.objects.get_or_create(user=cls.instance_seller)

        cls.seller_2_updated = {"username": "alexiaPATCH"}

        cls.seller_login = {
            "username": "alexia",
            "password": "1234",
        }

        cls.seller_login_error = {
            "username": "alexia",
            "password": "12343",
        }

        cls.admin = {
            "username": "abner",
            "first_name": "abner",
            "last_name": "leals",
            "password": "1234",
            "is_superuser": True,
            "is_seller": False,
        }

        cls.instance_admin = User.objects.create_user(**cls.admin)
        cls.token_admin = Token.objects.get_or_create(user=cls.instance_admin)

        cls.user_common = {
            "username": "lesley",
            "first_name": "lesley",
            "last_name": "silva",
            "password": "1234",
            "is_seller": False,
        }

        cls.user_deactivated = {
            "username": "pumba",
            "first_name": "marlco",
            "last_name": "polo",
            "password": "1234",
            "is_seller": False,
            "is_active": False,
        }

        cls.instance_user_deactivated = User.objects.create_user(**cls.user_deactivated)
