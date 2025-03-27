from django.contrib import admin
from .models import Rating, Recipe, SavedRecipe

# Register your models here.
admin.site.register(Rating)
admin.site.register(Recipe)
admin.site.register(SavedRecipe)
