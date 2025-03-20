from django.shortcuts import render
from .models import Category
from account.models import Recipe

# Create your views here.


def show_category(request, category_name_slug):
    context_dict = {}

    category = Category.objects.get(slug=category_name_slug)

    recipes = Recipe.objects.filter(category_id=category.id)

    context_dict["category"] = category
    context_dict["recipes"] = recipes

    return render(request, "category/index.html", context_dict)
