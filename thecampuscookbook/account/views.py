from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect,render
from recipe.models import SavedRecipe
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from recipe.forms import RecipeForm
from category.models import Category


@login_required
def saved_recipes(request):
    # Get the most recent save ID for each recipe
    latest_ids = SavedRecipe.objects.filter(
        user_profile=request.user.userprofile
    ).values('recipe').annotate(
        latest_id=Max('id')
    ).values_list('latest_id', flat=True)
    
    # Get complete SavedRecipe objects ordered by save time
    saved_recipes_list = SavedRecipe.objects.filter(
        id__in=latest_ids
    ).select_related('recipe').order_by('-saved_at')
    
    # Paginate the results
    paginator = Paginator(saved_recipes_list, 6)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return render(request, "account/saved-recipes/index.html", {
        'page_obj': page_obj,
        'total_recipes': saved_recipes_list.count()
    })

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

