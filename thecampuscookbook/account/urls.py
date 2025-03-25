from django.urls import path
import account.views as views

urlpatterns = [
    path("my-recipes/", views.my_recipes, name="my-recipes"),
    path("add-recipe/", views.add_recipe, name="add-recipe"),
    path("saved-recipes/", views.saved_recipes, name="saved-recipes"),
    path("settings/", views.settings, name="settings"),
]
