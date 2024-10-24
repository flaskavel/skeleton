from flaskavel.lab.alchemist.http.base_middleware import BaseMiddleware

class VerifyCsrfToken(BaseMiddleware):

    def handle(self, request, next, id):
        print(id)
        exit()