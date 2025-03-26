from django.urls import path
from .views import rate_recipe, save_recipe, remove_recipe, get_recipe

urlpatterns = [
    path("rate/", rate_recipe, name="rate_recipe"),
    path("save/", save_recipe, name="save_recipe"),
    path("remove/", remove_recipe, name="remove_recipe"),
    path("get/", get_recipe, name="get_average_rating"),
]
