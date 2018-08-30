from django.http import HttpResponse


def secondary_view(request):
    """View for the secondary site.
    """
    return HttpResponse("<html>This is the secondary site</html>")
