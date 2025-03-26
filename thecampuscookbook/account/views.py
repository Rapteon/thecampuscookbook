from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from recipe.models import SavedRecipe
from django.contrib.auth.decorators import login_required
from recipe.forms import RecipeForm
from category.models import Category


@login_required
def saved_recipes(request):
    # Get ALL saved recipes (not filtered by user)
    saved_recipes_list = SavedRecipe.objects.all().select_related("recipe")

    # Paginate the results - show 6 recipes per page
    paginator = Paginator(saved_recipes_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "account/saved-recipes/index.html", {"page_obj": page_obj})


@login_required
def my_recipes(request):
    return render(request, "account/my-recipes/index.html")


@login_required
def add_recipe(request):
    # Save the form if POST request, otherwise show a blank form.
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe_form.instance.user_profile = request.user.userprofile
            recipe_form.save()
            return redirect("my-recipes")
        else:
            print(recipe_form.errors)
    else:
        recipe_form = RecipeForm()

    categories = Category.objects.all()
    return render(
        request,
        "account/add-recipes/index.html",
        {"recipe_form": recipe_form, "categories": categories},
    )


@login_required
def settings(request):
    return render(request, "account/settings/index.html")
