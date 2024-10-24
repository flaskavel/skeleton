from flaskavel.lab.reagents.request import Request
from flaskavel.lab.reagents.response import Response
from flaskavel.lab.alchemist.http.base_middleware import BaseMiddleware

class ExampleMiddleware(BaseMiddleware):

    def handle(self, next):
        return next()
