from rest_framework.views import status

from accounts.models import User
from _utils.mocks import Mocks


class AccountsTest(Mocks):
    def test_RegisterUser(self):

        print("Tentando criar um vendedor")
        msg = [
            "Deveria ser capaz de criar uma nova conta de usuario",
        ]
        response = self.client.post(self.rota_users, self.seller)
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
        response = self.client.post(self.rota_users, self.user_common_2)

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

    def test_update_owner_account(self):
        print("Tentando atualizar usuario")
        msg = ["Deveria ser possivel atualizar o usuario"]

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)
        response = self.client.patch(
            f"{self.rota_users}{self.instance_seller.id}/",
            self.seller_2_updated,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg[0])

    def test_update_account(self):

        user = self.client.post(self.rota_users, self.seller)
        login = User.objects.filter(**user.data)
        print("Tentando atualizar usuario incorretamente")
        msg = ["Não deveria ser possivel atualizar o usuario"]

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)
        response = self.client.patch(
            f"{self.rota_users}{login[0].id}/",
            self.seller_2_updated,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg[0])

    def test_activated_account(self):
        print("Tentando ativar usuario")

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin.key)
        msg = [
            "Deveria ser retornado status 200",
            "Deveria ser possivel administrador ativar conta",
        ]
        response = self.client.patch(
            f"{self.rota_users}{self.instance_user_deactivated.id}/management/",
            {"is_active": True},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg[0])
        self.assertEqual(response.data["is_active"], True, msg[1])

    def test_deactivated_account(self):
        print("Tentando desativar usuario")

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin.key)
        msg = [
            "Deveria ser retornado status 200",
            "Deveria ser possivel administrador desativar conta",
        ]
        response = self.client.patch(
            f"{self.rota_users}{self.instance_seller.id}/management/",
            {"is_active": False},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg[0])
        self.assertEqual(response.data["is_active"], False, msg[1])

    def test_can_list_all_users(self):
        print(" Testando listar todos os usuarios")
        msg = [
            "Deveria ser retornado status 200",
        ]
        response = self.client.get("/api/accounts/")

        self.assertEqual(response.status_code, 200, msg[0])
