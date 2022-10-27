from django.test import TestCase
from products.models import Product
from accounts.models import User


class ProductRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.usuario = {
            "username": "abner_leals",
            "first_name": "abner",
            "last_name": "silva",
            "password": "1234",
            "is_seller": True,
        }

        cls.vendedor = User.objects.create_user(**cls.usuario)

        cls.produto_dados = {
            "description": "pão de queijo de aeroporto",
            "price": 100.00,
            "quantity": 2,
            "seller": cls.vendedor,
        }

        cls.produto = Product.objects.create(**cls.produto_dados)

    def test_product_relations(self):
        print("Testando relacionamento produtos")
        self.assertEqual(self.produto.seller, self.vendedor)
