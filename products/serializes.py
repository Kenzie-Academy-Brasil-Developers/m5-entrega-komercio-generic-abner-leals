from accounts.serializer import UserSellerSerializer
from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["description", "price", "quantity", "is_active", "seller"]


class ProductDetailSerializer(serializers.ModelSerializer):

    seller = UserSellerSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
        read_only_fields = ["id", "seller"]
        extra_kwargs = {
            "is_active": {"default": True},
            "quantity": {"min_value": 0},
        }

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
