"""URLs for PUBLIC_DOMAIN.
"""
from django.urls import path

from .views import public_view

urlpatterns = [path(r"", public_view, name="public-site")]
