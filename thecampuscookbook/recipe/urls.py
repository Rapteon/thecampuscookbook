from django.urls import path
from . import views

urlpatterns = [
    path("rate/", views.rate_recipe, name="rate_recipe"),
    path("save/", views.save_recipe, name="save_recipe"),
    path("remove/", views.remove_recipe, name="remove_recipe"),
    path("get/", views.get_recipe, name="get_average_rating"),
    path("delete/", views.delete_recipe, name="delete_recipe"),
]
