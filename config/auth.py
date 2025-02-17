from orionis.luminate.contracts.config.config_interface import IConfig
from orionis.luminate.bootstrap.register import register
from orionis.luminate.config.dataclass.auth import Auth
from orionis.luminate.facades.environment import env

@register.config
class Config(IConfig):

    config = Auth(

        # ...

    )