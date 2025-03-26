import json
from django.http import HttpResponseBadRequest, JsonResponse
from recipe.models import Rating, Recipe
from django.db.models import Avg

# Create your views here.


def rate_recipe(request):
    if is_ajax_request(request):
        if request.method == "POST":
            data = json.load(request)

            rating_value = int(data.get("rating"))

            recipe_id = int(data.get("recipeId"))
            if is_already_rated(request, recipe_id):
                print("Already rated")
                return JsonResponse({"status": "already rated"}, status=200)

            if not is_rating_valid(rating_value):
                print("Invalid rating value")
                return JsonResponse(
                    {"status": "rating value out of bounds"}, status=400
                )

            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                user_profile = request.user.userprofile
                rating = Rating.objects.create(
                    recipe=recipe, user_profile=user_profile, rating=rating_value
                )
                recipe.average_rating = Rating.objects.filter(recipe=recipe).aggregate(
                    Avg("rating")
                )["rating__avg"]
                print(recipe.average_rating)
                rating.save()
                recipe.save()
                return JsonResponse({"status": "saved"}, status=200)
            except Recipe.DoesNotExist:
                print("Recipe not found")
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
