from django.urls import path
from .views import rate_recipe, save_recipe

urlpatterns = [
    path("rate/", rate_recipe, name="rate_recipe"),
    path("save/", save_recipe, name="save_recipe"),
]
