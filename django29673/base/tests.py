from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class Django29673TestCase(TestCase):
    """Demonstrates the problem described by Django ticket #29673.
    """

    def test_internal(self):
        """Do stuff with the internal use site.
        """
        response = self.client.get(reverse("internal-site"))
        self.assertEqual(response.status_code, 200)

    def test_public(self):
        """Do stuff with the public site.
        """
        response = self.client.get(
            reverse("public-site", urlconf=settings.PUBLIC_URLCONF),
            SERVER_NAME=settings.PUBLIC_DOMAIN,
        )
        self.assertEqual(response.status_code, 200)
