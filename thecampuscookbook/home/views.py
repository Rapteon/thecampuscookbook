from django.shortcuts import render

# Create your views here.


def index(request):
    test = {
        "title": "Home",
        "content": "Welcome to the Cookbook home page!",
    }
    return render(request, "home/index.html", test)
