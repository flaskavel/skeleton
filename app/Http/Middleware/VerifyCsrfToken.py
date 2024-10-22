from flaskavel.lab.alchemist.http.base_middleware import BaseMiddleware

class VerifyCsrfToken(BaseMiddleware):

    def handle(self, *args, **kwargs):
        print(*args, **kwargs)