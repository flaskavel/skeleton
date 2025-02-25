from orionis.luminate.contracts.config.i_config import IConfig
from orionis.luminate.config.auth import Auth

class Config(IConfig):

    config = Auth(

        #--------------------------------------------------------------------------
        # Additional Values
        #--------------------------------------------------------------------------
        # If your application requires additional configurations, you can define
        # them in this dictionary.
        #--------------------------------------------------------------------------

        custom = {}

    )