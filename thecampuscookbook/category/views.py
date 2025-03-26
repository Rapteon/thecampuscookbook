from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category
from recipe.models import Recipe

def show_category(request, category_name_slug):
    context_dict = {}
    category = Category.objects.get(slug=category_name_slug)
    
    # Get all recipes for this category
    recipes_list = Recipe.objects.filter(category_id=category.id).order_by('-created_at')
    
    # Paginate the results (6 items per page)
    paginator = Paginator(recipes_list, 6)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context_dict["category"] = category
    context_dict["page_obj"] = page_obj
    
    return render(request, "category/index.html", context_dict)