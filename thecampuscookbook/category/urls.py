from django.urls import path
from category import views

urlpatterns = [
    path(
        "<slug:category_name_slug>/",
        views.show_category,
        name="show_category",
    ),
]
