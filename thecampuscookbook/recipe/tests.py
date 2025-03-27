from django.test import TestCase
from recipe.models import Recipe, SavedRecipe, Rating
from category.models import Category
from account.models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os
from django.conf import settings
from datetime import datetime


class RecipeModelTest(TestCase):
    def setUp(self):
        """Set up test data that will be used across multiple tests"""
        # Create user and profile
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.profile = UserProfile.objects.create(
            user=self.user, avatar="images/avatars/test.jpg"
        )

        # Create category
        self.category = Category.objects.create(
            name="Test Category", description="Test Description"
        )

        # Recipe data
        self.recipe_data = {
            "user_profile": self.profile,
            "title": "Test Recipe",
            "origin": "Test Origin",
            "category_id": self.category,
            "ingredients": "Test Ingredients",
            "description": "Test Description",
            "preparation_time": "30 mins",
            "image": "images/recipes/test.jpg",
            "average_rating": 4,
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)

    def test_recipe_creation(self):
        """Test that a recipe can be created with all fields"""
        self.assertEqual(self.recipe.title, "Test Recipe")
        self.assertEqual(self.recipe.origin, "Test Origin")
        self.assertEqual(self.recipe.category_id, self.category)
        self.assertEqual(self.recipe.ingredients, "Test Ingredients")
        self.assertEqual(self.recipe.description, "Test Description")
        self.assertEqual(self.recipe.preparation_time, "30 mins")
        self.assertEqual(self.recipe.image.name, "images/recipes/test.jpg")
        self.assertEqual(self.recipe.average_rating, 4)
        self.assertTrue(self.recipe.created_at)

    def test_title_max_length(self):
        """Test that title field enforces max length"""
        long_title = "x" * 101  # 101 characters (max is 100)
        recipe = Recipe(**self.recipe_data)
        recipe.title = long_title
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_origin_max_length(self):
        """Test that origin field enforces max length"""
        long_origin = "x" * 101  # 101 characters (max is 100)
        recipe = Recipe(**self.recipe_data)
        recipe.origin = long_origin
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_default_image(self):
        """Test that default image is set when not provided"""
        recipe = Recipe.objects.create(
            user_profile=self.profile,
            title="No Image Recipe",
            origin="Test Origin",
            category_id=self.category,
            ingredients="Test",
            description="Test",
            preparation_time="30 mins",
        )
        self.assertEqual(recipe.image.name, "images/recipes/default.jpeg")

    def test_string_representation(self):
        """Test the __str__ method returns the recipe title"""
        self.assertEqual(str(self.recipe), self.recipe.title)

    def test_recipe_deleted_when_user_deleted(self):
        """Test that recipe is deleted when user is deleted (CASCADE)"""
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(user_profile__user_id=user_id)

    def test_recipe_deleted_when_category_deleted(self):
        """Test that recipe is deleted when category is deleted (CASCADE)"""
        category_id = self.category.id
        self.category.delete()
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(category_id=category_id)

    def tearDown(self):
        """Clean up any files created during tests"""
        try:
            if self.recipe.image:
                if os.path.isfile(self.recipe.image.path):
                    os.remove(self.recipe.image.path)
        except:
            pass


class SavedRecipeModelTest(TestCase):
    def setUp(self):
        """Set up test data for SavedRecipe tests"""
        # Create user and profile
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.profile = UserProfile.objects.create(
            user=self.user, avatar="images/avatars/test.jpg"
        )

        # Create category
        self.category = Category.objects.create(
            name="Test Category", description="Test Description"
        )

        # Create recipe
        self.recipe = Recipe.objects.create(
            user_profile=self.profile,
            title="Test Recipe",
            origin="Test Origin",
            category_id=self.category,
            ingredients="Test Ingredients",
            description="Test Description",
            preparation_time="30 mins",
        )

        # Create saved recipe
        self.saved_recipe = SavedRecipe.objects.create(
            user_profile=self.profile, recipe=self.recipe
        )

    def test_saved_recipe_creation(self):
        """Test that a saved recipe can be created"""
        self.assertEqual(self.saved_recipe.user_profile, self.profile)
        self.assertEqual(self.saved_recipe.recipe, self.recipe)
        self.assertTrue(self.saved_recipe.saved_at)

    def test_string_representation(self):
        """Test the __str__ method returns the correct format"""
        expected_str = (
            f"SavedRecipe:Recipe={self.recipe} saved by UserProfile={self.profile}"
        )
        self.assertEqual(str(self.saved_recipe), expected_str)

    def test_saved_recipe_deleted_when_user_deleted(self):
        """Test that saved recipe is deleted when user is deleted (CASCADE)"""
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(SavedRecipe.DoesNotExist):
            SavedRecipe.objects.get(user_profile__user_id=user_id)

    def test_saved_recipe_deleted_when_recipe_deleted(self):
        """Test that saved recipe is deleted when recipe is deleted (CASCADE)"""
        recipe_id = self.recipe.id
        self.recipe.delete()
        with self.assertRaises(SavedRecipe.DoesNotExist):
            SavedRecipe.objects.get(recipe_id=recipe_id)


class RatingModelTest(TestCase):
    def setUp(self):
        """Set up test data for Rating tests"""
        # Create user and profile
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.profile = UserProfile.objects.create(
            user=self.user, avatar="images/avatars/test.jpg"
        )

        # Create category
        self.category = Category.objects.create(
            name="Test Category", description="Test Description"
        )

        # Create recipe
        self.recipe = Recipe.objects.create(
            user_profile=self.profile,
            title="Test Recipe",
            origin="Test Origin",
            category_id=self.category,
            ingredients="Test Ingredients",
            description="Test Description",
            preparation_time="30 mins",
        )

        # Create rating
        self.rating = Rating.objects.create(
            recipe=self.recipe, user_profile=self.profile, rating=4
        )

    def test_rating_creation(self):
        """Test that a rating can be created"""
        self.assertEqual(self.rating.recipe, self.recipe)
        self.assertEqual(self.rating.user_profile, self.profile)
        self.assertEqual(self.rating.rating, 4)

    def test_string_representation(self):
        """Test the __str__ method returns the correct format"""
        expected_str = f"Recipe='{self.recipe}' Rating='4' Username='{self.profile}'"
        self.assertEqual(str(self.rating), expected_str)

    def test_rating_deleted_when_recipe_deleted(self):
        """Test that rating is deleted when recipe is deleted (CASCADE)"""
        recipe_id = self.recipe.id
        self.recipe.delete()
        with self.assertRaises(Rating.DoesNotExist):
            Rating.objects.get(recipe_id=recipe_id)

    def test_rating_deleted_when_user_deleted(self):
        """Test that rating is deleted when user is deleted (CASCADE)"""
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(Rating.DoesNotExist):
            Rating.objects.get(user_profile__user_id=user_id)
