from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, "app/home.html", context)


def register(request):
    context = {}
    return render(request, "app/register.html", context)


def login(request):
    context = {}
    return render(request, "app/login.html", context)


def account(request):
    context = {}
    return render(request, "app/account.html", context)


def add_recipe(request):
    context = {}
    return render(request, "app/add_recipe.html", context)
