from rest_framework.permissions import BasePermission


class Is_Seller(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method == "GET"
            or (request.user.is_authenticated and (request.user.is_seller))
        )


class Is_Seller_Owner(BasePermission):
    def has_object_permission(self, request, view, product):

        return bool(request.method == "GET" or (product.seller.id == request.user.id))
