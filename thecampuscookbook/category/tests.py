from django.test import TestCase
from category.models import Category
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError


class CategoryModelTest(TestCase):
    def setUp(self):
        """Set up test data that will be used across multiple tests"""
        self.category_data = {
            "name": "Test Category",
            "description": "This is a test category description",
        }
        self.category = Category.objects.create(**self.category_data)

    def test_category_creation(self):
        """Test that a category can be created with required fields"""
        self.assertEqual(self.category.name, self.category_data["name"])
        self.assertEqual(self.category.description, self.category_data["description"])
        self.assertTrue(self.category.slug)  # Slug should be auto-generated

    def test_slug_auto_generation(self):
        """Test that slug is automatically generated from name"""
        self.assertEqual(self.category.slug, "test-category")

    def test_slug_uniqueness(self):
        """Test that slugs must be unique"""
        # Try to create another category with same name (should generate same slug)
        with self.assertRaises(IntegrityError):
            Category.objects.create(name="Test Category", description="Duplicate")

    def test_name_max_length(self):
        """Test that name field enforces max length"""
        long_name = "x" * 101  # 101 characters (max is 100)
        category = Category(name=long_name, description="Test")
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_description_max_length(self):
        """Test that description field enforces max length"""
        long_desc = "x" * 301  # 301 characters (max is 300)
        category = Category(name="Test", description=long_desc)
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_verbose_name_plural(self):
        """Test that the plural name is correctly set in Meta"""
        self.assertEqual(Category._meta.verbose_name_plural, "Categories")

    def test_string_representation(self):
        """Test the __str__ method returns the category name"""
        self.assertEqual(str(self.category), self.category.name)

    def test_slug_updates_when_name_changes(self):
        """Test that slug updates when name is changed"""
        original_slug = self.category.slug
        self.category.name = "Updated Category Name"
        self.category.save()
        self.assertNotEqual(self.category.slug, original_slug)
        self.assertEqual(self.category.slug, "updated-category-name")

    def test_name_required(self):
        """Test that name is a required field"""
        category = Category(description="Missing name")
        with self.assertRaises(ValidationError):
            category.full_clean()
