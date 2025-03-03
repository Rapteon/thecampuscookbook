from django.urls import path
from app import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("account/", views.account, name="account"),
    path("add_recipe/", views.add_recipe, name="add_recipe"),
]
