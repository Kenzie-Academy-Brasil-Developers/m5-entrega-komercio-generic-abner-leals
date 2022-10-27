from rest_framework.views import status

from accounts.models import User
from accounts.tests.mocks import Mocks


class AccountsTest(Mocks):
    def test_RegisterUser(self):

        print("Tentando criar um vendedor")
        msg = [
            "Deveria ser capaz de criar uma nova conta de usuario",
        ]
        response = self.client.post(self.rota_register, self.seller)
        # ipdb.set_trace()
        expected_status = status.HTTP_201_CREATED
        result_status = response.status_code

        self.assertEqual(expected_status, result_status, msg[0])
        chaves = {
            "username": "login",
            "first_name": "nome",
            "last_name": "sobrenome",
            "is_seller": "vendedor",
        }
        for key, value in chaves.items():
            self.assertEqual(
                self.seller[key],
                response.data[key],
                f"O esperado na chave {key} é `{value}` e foi recebido `{response.data[key]}`",
            )

    def test_ResgiterCommonUser(self):
        print("Tentando criar um usuario comum")

        msg = [
            "Deveria ser capaz de criar uma nova conta de usuario",
        ]
        response = self.client.post(self.rota_register, self.user_common)
        # ipdb.set_trace()
        expected_status = status.HTTP_201_CREATED
        result_status = response.status_code

        self.assertEqual(expected_status, result_status, msg[0])

    def test_login(self):
        print("Tentando login de usuario")
        msg = [
            "Espera-se status code igual a 200.",
            "Deveria ser capaz de retornar um token do usuario",
        ]
        response = self.client.post(self.rota_login, self.seller_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg[0])
        self.assertTrue(response.data["token"], msg[1])

    def test_error_login(self):
        print("Tentando logar com credenciais incorretas")
        msg = [
            "Espera-se status code igual a 400.",
        ]
        response = self.client.post(self.rota_login, self.seller_login_error)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg[0])
