from django.test import TestCase
from accounts.models import User
from products.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = {
            "username": "andresilva",
            "first_name": "andre",
            "last_name": "leal",
            "password": "1234",
            "is_seller": True,
        }

        cls.vendedor = User.objects.create_user(**cls.user)

        cls.produto = {
            "description": "pão de queijo de aeroporto",
            "price": 100.00,
            "quantity": 2,
            "seller": cls.vendedor,
        }

        cls.products = Product.objects.create(**cls.produto)

    def test_product_atributes(self):
        print("Testando Model Produtos")
        product = Product.objects.get(pk=self.products.id)

        self.assertEquals(product.description, self.produto["description"])
        self.assertEquals(product.price, self.produto["price"])
        self.assertEquals(product.quantity, self.produto["quantity"])
        self.assertEquals(product.seller, self.produto["seller"])
