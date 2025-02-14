from flaskavel.luminate.contracts.config.config_interface import IConfig
from flaskavel.luminate.bootstrap.register import register
from flaskavel.luminate.config.dataclass.auth import Auth
from flaskavel.luminate.facades.environment import env

@register.config
class Config(IConfig):

    config = Auth(

        # ...

    )