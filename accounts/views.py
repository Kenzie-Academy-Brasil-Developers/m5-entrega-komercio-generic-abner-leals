from rest_framework import views
from accounts.models import User

from accounts.serializer import LoginUserSerializer, UserSerializer

from common.common_view import GetCommonView, GetPostView, PostCommonView


from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserView(GetPostView):
    queryset = User.objects
    serializer_class = UserSerializer


class AccountDetailView(GetPostView):
    queryset = User.objects
    serializer_class = UserSerializer

    def get_queryset(self):
        lista_max = self.kwargs["num"]

        return self.queryset.order_by("-date_joined")[0:lista_max]


class LoginView(views.APIView):
    def post(self, request: views.Request) -> views.Response:
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return views.Response(
                {"detail": "invalid username or password"},
                views.status.HTTP_400_BAD_REQUEST,
            )

        token, _ = Token.objects.get_or_create(user=user)

        return views.Response({"token": token.key}, views.status.HTTP_200_OK)