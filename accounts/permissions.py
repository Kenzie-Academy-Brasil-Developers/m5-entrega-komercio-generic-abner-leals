from rest_framework.permissions import BasePermission


class Is_Admin(BasePermission):
    def has_permission(self, request, view):
        return bool((request.user.is_authenticated and (request.user.is_superuser)))


class Is_Account_Owner(BasePermission):
    def has_object_permission(self, request, view, account):

        if request.user.is_superuser:
            return True
        if request.user.is_authenticated and account.id == request.user.id:
            return True
