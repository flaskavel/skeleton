from app.Http.Controllers import HomeController
from flaskavel.lab.alchemist.http.base_controller import BaseController

class Route:

    @staticmethod
    def middleware(middleware:list = []):
        instance = RouteManager()
        return instance.middleware(middleware)

    @staticmethod
    def controller(instance:object):

        if not isinstance(instance, BaseController):
            raise ValueError("El objeto suministrado no es un controlador valido.")

        instance = RouteManager()
        return instance.controller(instance)

    @staticmethod
    def prefix(prefix:str):
        instance = RouteManager()
        return instance.prefix(prefix)

    @staticmethod
    def group(*argv, **kwargs):
        pass

    @staticmethod
    def get():
        pass

    @staticmethod
    def post():
        pass

    @staticmethod
    def put():
        pass

    @staticmethod
    def patch():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def options():
        pass

class RouteManager:

    def __init__(self):
        self._middleware = []

    def middleware(self, middleware:list = []):
        self._middleware = middleware
        return self

    def controller(self):
        return self

    def prefix(self):
        return self

    def group(self):
        return self

    def get(self):
        return self

    def post(self):
        return self

    def put(self):
        return self

    def patch(self):
        return self

    def delete(self):
        return self

    def options(self):
        return self




Route.middleware(['first', 'second']).controller(HomeController).prefix('admin').group(
    Route.get('/user', 'index').name('index.users'),
)