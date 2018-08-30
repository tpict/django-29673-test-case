from django.conf import settings
from django.urls import set_urlconf


class MultipleDomainMiddleware(object):
    """Middleware for delivering different urlconfs for different domains.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.process_request(request)

    def process_request(self, request):
        """Assign the urlconf for the requested domain.
        """
        if request.path.split("/")[1] == "secondary":
            request.urlconf = "django29673.secondary.urls"

        return self.get_response(request)

        # To make tests pass, comment the return statement and uncomment this
        # block:
        # try:
        #     return self.get_response(request)
        # finally:
        #     if getattr(request, "urlconf", None) is not None:
        #         set_urlconf(None)
