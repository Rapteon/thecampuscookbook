from django.urls import path
from category.views import soup as category_soup
from category.views import starter as category_starter
from category.views import main as category_main
from category.views import dessert as category_dessert
from category.views import creative as category_creative

urlpatterns = [
    path("soup/", category_soup, name="category-soup"),
    path("starter/", category_starter, name="category-starter"),
    path("main/", category_main, name="category-main"),
    path("dessert/", category_dessert, name="category-dessert"),
    path("creative/", category_creative, name="category-creative"),
]
