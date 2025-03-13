from django.shortcuts import render

# Create your views here.


def soup(request):
    return render(request, "category/soup/index.html")


def starter(request):
    return render(request, "category/starter/index.html")


def main(request):
    return render(request, "category/main/index.html")


def dessert(request):
    return render(request, "category/dessert/index.html")


def creative(request):
    return render(request, "category/creative/index.html")
