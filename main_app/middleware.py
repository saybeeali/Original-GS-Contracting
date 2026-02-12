from django.http import HttpResponsePermanentRedirect

class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        # If the request is coming from the old Fly address
        if host == 'original-gs-contracting.fly.dev':
            # Shift them to the new professional domain
            return HttpResponsePermanentRedirect(
                f"https://www.gscontractingny.com{request.get_full_path()}"
            )
        
        return self.get_response(request)