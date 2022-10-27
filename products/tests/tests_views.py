from rest_framework.views import status

from accounts.models import User
from products.models import Product
from _utils.mocks import Mocks


class ProductTest(Mocks):
    def test_product_create_seller(self):
        print("Testando criação de produto")
        msg = [
            "Deveria ser retornar codigo de status 201",
        ]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)
        response = self.client.post(self.rota_products, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg[0])

    def test_product_create_common_account(self):
        print("Testando criação de produto com usuario comun")
        msg = [
            "Deveria ser retornar codigo de status 403",
        ]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_common.key)
        response = self.client.post(self.rota_products, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg[0])

    def test_product_create_wrong_keys(self):
        print("Testando criação de produto com atributos errados")
        msg = [
            "Deveria ser retornar codigo de status 400",
        ]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)

        response = self.client.post(self.rota_products, self.product_data_wrong_keys)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg[0])

    def test_product_update_seller_account(self):
        print("Testando atualização de produto")
        msg = [
            "Deveria ser retornar codigo de status 200",
        ]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)
        response = self.client.patch(
            f"{self.rota_products}{self.instance_product.id}/",
            self.product_updated_data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg[0])

    def test_product_update_common_account(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_common.key)
        print("Testando atualização de produto com usuario comum")
        msg = [
            "Deveria ser retornar codigo de status 403",
        ]

        response = self.client.patch(
            f"{self.rota_products}{self.instance_product.id}/",
            self.product_updated_data,
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg[0])

    def test_product_list(self):
        print("Testando listagem de produtos")
        msg = [
            "Deveria ser retornar codigo de status 200",
            "Não deveria retornar mais que 2 objetos por listagem ",
        ]
        response = self.client.get(self.rota_products)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg[0])
        self.assertTrue(response.data["count"] <= 2, msg[1])
