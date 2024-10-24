from flaskavel.lab.alchemist.http.base_controller import BaseController
from flaskavel.lab.reagents.response import Response
from flaskavel.lab.app import Application

class ExampleController(BaseController):

    def index(self):
        return Response.success(
            data={
                'framework' : Application.name.upper(),
                'version' : Application.version,
            },
            message="Welcome Aboard"
        )