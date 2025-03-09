from django.utils.timezone import timezone
from tkinter import CASCADE
from django.db import models


class USERS(models.Model):
    user_id = models.AutoField(primary_key=True)
    avatar_image = models.ImageField(upload_to='/media/',blank=True,null=True)
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200,unique = True)
    email = models.EmailField(max_length=150,unique=True)
    password = models.CharField(max_length=128,)
    join_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.user_name

class RECIPES(models.Model):
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

class COMMENTS(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(USERS,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(RECIPES,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f"Comment by {self.user.user_name} on {self.recipe.title}"

class RATINGS(models.Model):
    rating_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(USERS,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(RECIPES,on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    def __str__(self):
        return f"Rating by {self.user.user_name} on {self.recipe.title}"

class SAVED_RECIPES(models.Model):
    saved_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(USERS,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(RECIPES,on_delete=models.CASCADE)
    saved_at = models.DateTimeField(default = timezone.now)
    def __str__(self):
        f"{self.recipe.title} saved by {self.user.user_name}"