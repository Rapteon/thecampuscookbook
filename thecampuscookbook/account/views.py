from django.shortcuts import render

# Create your views here.


def my_recipes(request):
    return render(request, "account/my-recipes/index.html")


def add_recipe(request):
    return render(request, "account/add-recipes/index.html")


def saved_recipes(request):
    return render(request, "account/saved-recipes/index.html")


def settings(request):
    return render(request, "account/settings/index.html")
