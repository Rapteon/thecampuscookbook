from django.shortcuts import render
from recipe.models import Recipe

# Create your views here.


def index(request):
    latest_recipes = Recipe.objects.order_by("-created_at")[:2]
    context_dict = {
        "title": "Home",
        "content": "Welcome to the Cookbook home page!",
        "latest_recipes": latest_recipes,
    }
    return render(request, "home/index.html", context_dict)
