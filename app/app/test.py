
"""
Sample tests
"""

from django.test import SimpleTestCase
from app.calc import add, subtract


class CalcTests(SimpleTestCase):
    """Simple smoke tests for the recipe app."""

    def test_add_integers(self):
        self.assertEqual(add(5, 6), 11)

    def test_subtract_integers(self):
        self.assertEqual(subtract(10, 15), -5)
