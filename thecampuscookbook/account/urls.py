from django.urls import path
from account.views import my_recipes
from account.views import add_recipe
from account.views import saved_recipes
from account.views import settings

urlpatterns = [
    path("my-recipes/", my_recipes, name="my-recipes"),
    path("add-recipe/", add_recipe, name="add-recipe"),
    path("saved-recipes/", saved_recipes, name="saved-recipes"),
    path("settings/", settings, name="settings"),
]
