from flaskavel.luminate.contracts.config.config_interface import IConfig
from flaskavel.luminate.config.dataclass.app import Data
from flaskavel.luminate.facades.environment import env

class App(IConfig):

    config = Data(

        #--------------------------------------------------------------------------
        # Application Name
        #--------------------------------------------------------------------------
        # This value is the name of the application, useful for notifications,
        # UI elements, or whenever the application's name needs to be displayed.
        #--------------------------------------------------------------------------

        name = env('APP_NAME', 'Flaskavel'),

        #--------------------------------------------------------------------------
        # Application Debug Mode
        #--------------------------------------------------------------------------
        # Value used to show detailed error information when an error occurs in
        # the application, useful for deciding whether or not to display details.
        #--------------------------------------------------------------------------

        debug = env('APP_DEBUG', False),

        #--------------------------------------------------------------------------
        # Application Bytecode
        #--------------------------------------------------------------------------
        # This value determines if the application should run by creating bytecode
        # files, useful if you don't want these files in a dev environment.
        #--------------------------------------------------------------------------

        bytecode = env('APP_BYTECODE', True),

        #--------------------------------------------------------------------------
        # Application Timezone
        #--------------------------------------------------------------------------
        # Value used to set the application's timezone, useful if a different
        # timezone is needed.
        #--------------------------------------------------------------------------

        timezone = env('APP_TIMEZONE', 'UTC'),

        #--------------------------------------------------------------------------
        # Application URL
        #--------------------------------------------------------------------------
        # Value used to determine the application's URL, useful when you need to
        # access the URL anywhere in the framework without accessing the ".env" file.
        #--------------------------------------------------------------------------

        url = env('APP_URL', '127.0.0.1'),
        port = env('APP_PORT', 8080),

        #--------------------------------------------------------------------------
        # Application Encryption
        #--------------------------------------------------------------------------
        # Values used to define the encryption supported by the framework,
        # supporting 128, 192, 256-bit keys.
        #--------------------------------------------------------------------------

        cipher = 'AES-256-GCM',
        key = env('APP_KEY')

    )