from django.test import TestCase
from django.urls import reverse


class PrimaryTestCase(TestCase):
    """Demonstrates the problem described by Django ticket #29673.
    """

    def test_primary(self):
        """Do stuff with the primary site.
        """
        response = self.client.get(reverse("primary-site"))
        self.assertEqual(response.status_code, 200)

    def test_secondary(self):
        """Do stuff with the secondary site.
        """
        response = self.client.get(
            reverse("secondary-site", urlconf="django29673.secondary.urls")
        )
        self.assertEqual(response.status_code, 200)
