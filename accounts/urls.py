from django.urls import path

from accounts import views

urlpatterns = [
    path("accounts/", views.UserView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("accounts/newest/<int:num>/", views.AccountNewestView.as_view()),
    path("accounts/<pk>/", views.AccountDetailView.as_view()),
    path("accounts/<pk>/management/", views.AdminDetailView.as_view()),
]
