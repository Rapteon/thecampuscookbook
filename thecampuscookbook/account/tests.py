from django.test import TestCase
from account.models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os
from django.conf import settings

class UserProfileModelTest(TestCase):
    def setUp(self):
        """Set up test data that will be used across multiple tests"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile_data = {
            'user': self.user,
            'avatar': 'images/avatars/test.jpg'
        }
        self.profile = UserProfile.objects.create(**self.profile_data)

    def test_user_profile_creation(self):
        """Test that a user profile can be created with required fields"""
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.avatar.name, 'images/avatars/test.jpg')

    def test_default_avatar(self):
        """Test that default avatar is set when not provided"""
        new_user = User.objects.create_user(
            username='newuser',
            password='newpass123'
        )
        new_profile = UserProfile.objects.create(user=new_user)
        self.assertEqual(
            new_profile.avatar.name,
            'images/avatars/default.png'
        )

    def test_one_to_one_relationship(self):
        """Test the one-to-one relationship with User model"""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.user.userprofile, self.profile)

    def test_verbose_name_plural(self):
        """Test that the plural name is correctly set in Meta"""
        self.assertEqual(
            UserProfile._meta.verbose_name_plural,
            'UserProfiles'
        )

    def test_string_representation(self):
        """Test the __str__ method returns the correct format"""
        expected_str = f"Username: {self.user.username} Avatar: {self.profile.avatar.name}"
        self.assertEqual(str(self.profile), expected_str)

    def test_user_required(self):
        """Test that user field is required"""
        profile = UserProfile(avatar='images/avatars/test.jpg')
        with self.assertRaises(ValidationError):
            profile.full_clean()

    def test_avatar_upload_path(self):
        """Test that avatar is uploaded to the correct path"""
        self.assertTrue(
            self.profile.avatar.name.startswith('images/avatars/')
        )

    def test_profile_deleted_when_user_deleted(self):
        """Test that profile is deleted when user is deleted (CASCADE)"""
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(UserProfile.DoesNotExist):
            UserProfile.objects.get(user_id=user_id)

    def test_avatar_file_handling(self):
        """Test avatar file handling (simulated)"""
        # This would be more comprehensive with actual file upload tests
        self.profile.avatar = 'images/avatars/new.jpg'
        self.profile.save()
        self.assertEqual(self.profile.avatar.name, 'images/avatars/new.jpg')

    def tearDown(self):
        """Clean up any files created during tests"""
        try:
            if self.profile.avatar:
                if os.path.isfile(self.profile.avatar.path):
                    os.remove(self.profile.avatar.path)
        except:
            pass
