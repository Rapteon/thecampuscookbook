import json
from django.http import HttpResponseBadRequest, JsonResponse
from recipe.models import Rating, Recipe, SavedRecipe
from django.db.models import Avg

# Create your views here.


def rate_recipe(request):
    if is_ajax_request(request):
        if request.method == "POST":
            data = json.load(request)

            print(data)
            rating_value = int(data.get("rating"))

            recipe_id = int(data.get("recipeId"))
            if is_already_rated(request, recipe_id):
                return JsonResponse({"status": "already rated"}, status=200)

            if not is_rating_valid(rating_value):
                print(rating_value)
                return JsonResponse(
                    {"status": "rating value out of bounds"}, status=400
                )

            try:
                print("In try of rating")
                recipe = Recipe.objects.get(pk=recipe_id)
                user_profile = request.user.userprofile
                rating = Rating.objects.create(
                    recipe=recipe, user_profile=user_profile, rating=rating_value
                )
                recipe.average_rating = Rating.objects.filter(recipe=recipe).aggregate(
                    Avg("rating")
                )["rating__avg"]
                rating.save()
                recipe.save()
                return JsonResponse({"status": "rated"}, status=200)
            except Recipe.DoesNotExist:
                return JsonResponse({"status": "not found"}, status=404)
        else:
            return HttpResponseBadRequest("Does not accept GET requests.")
    else:
        print(request.headers)
        return HttpResponseBadRequest("Only accepts AJAX requests.")


def is_rating_valid(rating: int):
    return rating <= 5 and rating >= 0


def is_ajax_request(request):
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


def is_already_rated(request, recipe_id: int):
    """Checks if the recipe was already rated by the user"""
    try:
        ratings = Rating.objects.filter(
            recipe=recipe_id, user_profile=request.user.userprofile
        )
        print(ratings)
        return len(ratings) > 0
    except IndexError:
        return False
    except Rating.DoesNotExist:
        return False


def save_recipe(request):
    """Saves a recipe for the user"""
    if is_ajax_request(request):
        if request.method == "POST":
            data = json.load(request)

            recipe_id = int(data.get("recipeId"))

            if is_already_saved(request, recipe_id):
                return JsonResponse({"status": "already saved"}, status=200)

            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                user_profile = request.user.userprofile
                saved_recipe = SavedRecipe.objects.create(
                    recipe=recipe, user_profile=user_profile
                )
                saved_recipe.save()
                return JsonResponse({"status": "saved"}, status=200)

            except Recipe.DoesNotExist:
                return JsonResponse({"status": "not found"}, status=404)
        else:
            return HttpResponseBadRequest("Does not accept GET requests.")
    else:
        return HttpResponseBadRequest("Only accepts AJAX requests.")


def is_already_saved(request, recipe_id):
    """Checks if the recipe was already saved by the user"""
    try:
        saved_recipe = SavedRecipe.objects.filter(
            recipe=recipe_id, user_profile=request.user.userprofile
        )
        return len(saved_recipe) > 0
    except IndexError:
        return False
    except Rating.DoesNotExist:
        return False


def remove_recipe(request):
    if is_ajax_request(request):
        if request.method == "POST":
            data = json.load(request)

            recipe_id = int(data.get("recipeId"))

            print(recipe_id)
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                print(recipe)
                user_profile = request.user.userprofile
                saved_recipe = SavedRecipe.objects.get(
                    recipe=recipe, user_profile=user_profile
                )
                print(saved_recipe)
                saved_recipe.delete()
                return JsonResponse({"status": "removed"}, status=200)

            except Recipe.DoesNotExist:
                return JsonResponse({"status": "not found"}, status=404)
        else:
            return HttpResponseBadRequest("Does not accept GET requests.")
    else:
        print(request.headers)
        return HttpResponseBadRequest("Only accepts AJAX requests.")


def get_recipe(request):
    """Returns a recipe by its id"""
    if is_ajax_request(request):
        if request.method == "POST":
            data = json.load(request)

            recipe_id = int(data.get("recipeId"))

            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                json_recipe = json.dumps(
                    {
                        "id": recipe.id,
                        "title": recipe.title,
                        "description": recipe.description,
                        "origin": recipe.origin,
                        "category": recipe.category_id.name,
                        "ingredients": recipe.ingredients,
                        "preparation_time": recipe.preparation_time,
                        "average_rating": recipe.average_rating,
                    }
                )
                return JsonResponse(
                    {"status": "found", "recipe": json_recipe}, status=200
                )

            except Recipe.DoesNotExist:
                return JsonResponse({"status": "not found"}, status=404)
        else:
            return HttpResponseBadRequest("Does not accept GET requests.")
    else:
        print(request.headers)
        return HttpResponseBadRequest("Only accepts AJAX requests.")


def delete_recipe(request):
    if is_ajax_request(request):
        if request.method == "POST":
            data = json.load(request)

            recipe_id = int(data.get("recipeId"))

            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                recipe.delete()
                return JsonResponse({"status": "deleted"}, status=200)

            except Recipe.DoesNotExist:
                return JsonResponse({"status": "not found"}, status=404)
        else:
            return HttpResponseBadRequest("Does not accept GET requests.")
    else:
        print(request.headers)
        return HttpResponseBadRequest("Only accepts AJAX requests.")
