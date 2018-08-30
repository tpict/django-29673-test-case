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
        host = request.get_host()
        if host == settings.PUBLIC_DOMAIN:
            request.urlconf = settings.PUBLIC_URLCONF

        return self.get_response(request)

        # To make tests pass, comment the return statement and uncomment this
        # block:
        # try:
        #     return self.get_response(request)
        # finally:
        #     if getattr(request, "urlconf", None) is not None:
        #         set_urlconf(None)
