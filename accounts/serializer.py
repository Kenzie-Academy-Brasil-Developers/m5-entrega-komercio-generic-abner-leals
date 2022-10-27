from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "is_seller",
            "date_joined",
            "is_superuser",
            "is_active",
        ]

        read_only_fields = ["date_joined", "is_superuser", "is_active"]
        extra_kwargs = {"password": {"write_only": True}}
        validators = [
            UniqueTogetherValidator(queryset=User.objects.all(), fields=["username"]),
        ]

        # https://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer
        # https://www.geeksforgeeks.org/modelserializer-in-serializers-django-rest-framework/

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class UserSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        exclude = [
            "last_login",
            "is_staff",
            "is_active",
            "updated_at",
            "groups",
            "email",
            "user_permissions",
        ]
        read_only_fields = ["date_joined", "is_superuser", "is_active"]


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_seller",
            "date_joined",
            "is_superuser",
            "is_active",
        ]
        read_only_fields = [
            "date_joined",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
        ]
