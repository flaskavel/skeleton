from flaskavel.luminate.contracts.config.config_interface import IConfig
from flaskavel.luminate.config.dataclass.auth import Data
from flaskavel.luminate.facades.environment import env

class Auth(IConfig):

    config = Data(

        # ...

    )