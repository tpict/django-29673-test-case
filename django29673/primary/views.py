from django.http import HttpResponse


def primary_view(request):
    """View for the primary site.
    """
    return HttpResponse("<html>This is the primary site</html>")
