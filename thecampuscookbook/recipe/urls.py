from django.urls import path
from .views import rate_recipe

urlpatterns = [
    path("rate/", rate_recipe, name="rate_recipe"),
    # path('add/', views.add_recipe, name='add_recipe'),
    # path('edit/<int:id>/', views.edit_recipe, name='edit_recipe'),
    # path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
]
