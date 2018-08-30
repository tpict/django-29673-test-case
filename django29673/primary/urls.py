"""Primary URLs.
"""
from django.urls import path

from .views import primary_view

urlpatterns = [path("", primary_view, name="primary-site")]
