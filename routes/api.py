from app.Http.Controllers import HomeController

class Route:

    @staticmethod
    def middleware(middleware:list = []) -> 'RouteManager':
        instance = RouteManager()
        return instance.middleware(middleware)

    @staticmethod
    def controller(instance:object):
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
        pass

    def middleware(self):
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