from django.utils.timezone import timezone
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(USERS,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    preparation_time = models.CharField(max_length=100)
    created_at = models.DateTimeField(default = timezone.now)
    popularity = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    def __str__(self):
        return f"Rating by {self.user.user_name} on {self.recipe.title}"

class SavedRecipes(models.Model):
    saved_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    saved_at = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f"{self.recipe.title} saved by {self.user.user_name}"