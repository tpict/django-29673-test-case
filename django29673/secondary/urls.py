"""URLs for secondary_DOMAIN.
"""
from django.urls import path

from .views import secondary_view

urlpatterns = [path("secondary/", secondary_view, name="secondary-site")]
