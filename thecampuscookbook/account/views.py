from django.core.paginator import Paginator
from django.shortcuts import render
from recipe.models import SavedRecipe

def saved_recipes(request):
    # Get ALL saved recipes (not filtered by user)
    saved_recipes_list = SavedRecipe.objects.all().select_related('recipe')
    
    # Paginate the results - show 6 recipes per page
    paginator = Paginator(saved_recipes_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "account/saved-recipes/index.html", {
        'page_obj': page_obj
    })


def my_recipes(request):
    return render(request, "account/my-recipes/index.html")


def add_recipe(request):
    return render(request, "account/add-recipes/index.html")


def settings(request):
    return render(request, "account/settings/index.html")