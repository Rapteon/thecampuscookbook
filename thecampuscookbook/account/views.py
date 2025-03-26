from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from recipe.models import SavedRecipe
from django.contrib.auth.decorators import login_required
from django.db.models import Max



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
    return render(request, "account/add-recipes/index.html")


@login_required
def settings(request):
    return render(request, "account/settings/index.html")

