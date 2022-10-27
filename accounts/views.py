from rest_framework import views
from _project.pagination import CustomPageNumberPagination
from accounts.models import User
from accounts.permissions import Is_Account_Owner, Is_Admin

from accounts.serializer import LoginUserSerializer, UserAdminSerializer, UserSerializer

from _utils.common_view import GetCommonView, GetPostView, PostCommonView
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserView(GetPostView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountNewestView(GetPostView):
    queryset = User.objects
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        lista_max = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:lista_max]


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Is_Account_Owner]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [Is_Admin]
    authentication_classes = [TokenAuthentication]

    queryset = User.objects.all()
    serializer_class = UserAdminSerializer


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
