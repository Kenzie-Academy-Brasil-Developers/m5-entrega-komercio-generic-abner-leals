from products.models import Product
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.models import User


class Mocks(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.rota_users = "/api/accounts/"
        cls.rota_login = "/api/login/"
        cls.rota_products = "/api/products/"
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
        cls.token_seller, _ = Token.objects.get_or_create(user=cls.instance_seller)

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
        cls.token_admin, _ = Token.objects.get_or_create(user=cls.instance_admin)

        cls.user_common = {
            "username": "raquel",
            "first_name": "raquel",
            "last_name": "santos",
            "password": "1234",
            "is_seller": False,
        }
        cls.user_common_2 = {
            "username": "lesley",
            "first_name": "lesley",
            "last_name": "silva",
            "password": "1234",
            "is_seller": False,
        }
        cls.instance_common = User.objects.create_user(**cls.user_common)
        cls.token_common, _ = Token.objects.get_or_create(user=cls.instance_common)

        cls.user_deactivated = {
            "username": "pumba",
            "first_name": "marlco",
            "last_name": "polo",
            "password": "1234",
            "is_seller": False,
            "is_active": False,
        }

        cls.instance_user_deactivated = User.objects.create_user(**cls.user_deactivated)

        cls.product_data = {
            "description": "pão de queijo de aeroporto",
            "price": 100.00,
            "quantity": 2,
        }

        cls.instance_product = Product.objects.create(
            **cls.product_data, seller=cls.instance_seller
        )

        cls.product_updated_data = {
            "description": "pão de queijo de aeroporto atualizado"
        }

        cls.product_data_wrong_keys = {
            "dexcription": "pão de queijo de aeroporto",
            "praice": 100.00,
            "quantiti": 2,
        }
