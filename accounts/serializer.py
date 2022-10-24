from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        exclude = [
            "id",
            "last_login",
            "is_staff",
            "is_active",
            "updated_at",
            "groups",
            "email",
            "user_permissions",
        ]
        read_only_fields = ["date_joined", "is_superuser", "is_active"]
        # https://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer
        # https://www.geeksforgeeks.org/modelserializer-in-serializers-django-rest-framework/

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class UserSellerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()