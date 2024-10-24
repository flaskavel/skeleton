from flaskavel.lab.reagents.response import Response
from flaskavel.lab.alchemist.http.base_controller import BaseController

class HomeController(BaseController):

    def index(self, id, name):
        return Response.success(
            message="Desde Controlador Flaskavel"
        )