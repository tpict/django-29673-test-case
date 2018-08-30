from django.http import HttpResponse


def public_view(request):
    """View for the public site.
    """
    return HttpResponse("<html>This is the public site</html>")
