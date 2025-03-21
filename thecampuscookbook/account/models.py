from django.db import models

# Using built-in User model, hence not defining new class.
from django.contrib.auth.models import User
from recipe.models import Recipe


class Rating(models.Model):
    # Not creating rating_id as Django automatically adds an id field.
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"Recipe='{self.recipe_id}' Rating='{self.rating}' User='{self.user_id}'"
