from single_sign_on import SingleSignOnRegistry

class MyService:

    def __init__(self, sso_registry, *args, **kwargs):
        self.sso_registry = sso_registry

    def handle(self, request, sso_token):
        if self.sso_registry.is_valid(sso_token):
            return Response("Hello {0}!".format(request.name))
        else:
            return Response("Please sign in")


class Request:

    def __init__(self, name, *args, **kwargs):
        self.name = name

class Response:
    def __init__(self, text, *args, **kwargs):
        self.text = text