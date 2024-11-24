from pathlib import Path
from flaskavel.lab.app import Application

# --------------------------------------------------------------------------
# Bootstrapping Flaskavel
# --------------------------------------------------------------------------
# This file is responsible for initializing the application the first time it is executed
# and maintaining a valid cache in case there are changes in the files
# that make up the system. It will automatically adapt, making the execution faster
# than reloading the entire system for each request, whether it's CLI or HTTP.
# --------------------------------------------------------------------------

def app():
    """
    Initializes and configures the Flaskavel application.

    This function bootstraps the Flaskavel framework, setting up routing, middlewares,
    and the application environment. It ensures efficient reloading by maintaining a valid cache.

    Returns:
        Application: The configured Flaskavel application instance.
    """
    return Application.configure(
        base_path=Path(__file__).resolve().parent.parent,
    ).withRouting(
        api=['api'],
        web=['web'],
    ).withMiddlewares(
        aliases={
            'csrf': {'module': 'ExampleMiddleware', 'classname': 'ExampleMiddleware'},
        },
        use=[
            {'module': 'ExampleMiddleware', 'classname': 'ExampleMiddleware'},
        ]
    ).create()
