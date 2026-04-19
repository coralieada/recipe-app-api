"""
Tests for models.
"""
from django.test import TestCase # noqa F401
from django.contrib.auth import get_user_model # noqa F401


class ModelTests(TestCase):
    """Tests for models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ['test1@example.com', 'test1@example.com'],
            ['Test2@EXAMPLE.COM', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEassST3@example.com'],
            ['test4@example.Com', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email, password='testpass123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass123')

    def test_create_superuser(self):
        """Test creating a new superuser."""
        email = 'admin@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_superuser(
            email=email, password=password)

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
