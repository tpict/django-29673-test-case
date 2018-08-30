from django.http import HttpResponse


def internal_view(request):
    """View for the internal use site.
    """
    return HttpResponse("<html>This is the internal use site</html>")
