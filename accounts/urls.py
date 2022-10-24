from django.urls import path

from accounts.views import AccountDetailView, LoginView, UserView


urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/newest/<int:num>/", AccountDetailView.as_view()),
]
