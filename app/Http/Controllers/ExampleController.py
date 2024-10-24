from flaskavel.lab.alchemist.http.base_controller import BaseController
from flaskavel.lab.reagents.response import Response
from flaskavel.lab.app import Application

class ExampleController(BaseController):

    def index(self):
        """
        Handles the request for the 'index' endpoint. This method responds with basic
        information about the framework, such as its name and version.

        Returns:
            Response: A successful JSON response containing framework details.
        """
        return Response.success(
            data={
                'framework' : Application.name.upper(),
                'version' : Application.version,
            },
            message="Welcome Aboard"
        )