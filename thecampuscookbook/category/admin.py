from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """Custom class for Category to use with admin app"""

    # Prepopulate the slug field with the name field in Category.
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
