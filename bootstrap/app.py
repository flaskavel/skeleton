from pathlib import Path
from flaskavel.lab.app import Application

# Configure and initialize the application
__app = Application.configure(
            base_path = Path(__file__).resolve().parent.parent,
        ).withRouting(
            api = ('api',),
            web = ('web',),
        ).withMiddlewares(
            aliases = {
                'csrf_token' : 'VerifyCsrfToken',
            },
            use = [
                'VerifyCsrfToken',
            ]
        ).create()