from django.db import models

# Using built-in User model, hence not defining new class.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    avatar = models.ImageField(
        upload_to="images/avatars/", default="images/avatars/default.png"
    )

    def __str__(self):
        return f"Username: {self.user.username} Avatar: {self.avatar.name}"

    class Meta:
        verbose_name_plural = "UserProfiles"
