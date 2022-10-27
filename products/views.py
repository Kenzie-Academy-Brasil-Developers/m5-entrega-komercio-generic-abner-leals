from rest_framework import views, generics, exceptions
from _project.pagination import CustomPageNumberPagination
from _utils.mixin import SerializerByMethodMixin
from products.models import Product

from _utils.common_view import GetPostView

from rest_framework.authentication import TokenAuthentication

from products.permissions import Is_Seller, Is_Seller_Owner
from products.serializes import ProductSerializer, ProductDetailSerializer

from django.shortcuts import get_object_or_404


class ProductView(
    SerializerByMethodMixin,
    generics.ListCreateAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Is_Seller]
    pagination_class = CustomPageNumberPagination

    queryset = Product.objects.all()
    serializer_map = {
        "GET": ProductSerializer,
        "POST": ProductDetailSerializer,
    }

    def perform_create(self, serializer):
        seller = self.request.user
        serializer.save(seller=seller)


class DetailedProductView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Is_Seller_Owner]
    pagination_class = CustomPageNumberPagination

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
