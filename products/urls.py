from products.views import ProductView, DetailedProductView
from django.urls import path
from accounts.views import AccountDetailView, LoginView, UserView


urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<pk>/", DetailedProductView.as_view()),
]
