from orionis.contracts.config.i_config import IConfig
from orionis.luminate.config.app import App
from orionis.luminate.facades.environment.environment_facade import env

class Config(IConfig):

    config = App(

        #--------------------------------------------------------------------------
        # Application Name
        #--------------------------------------------------------------------------
        # Defines the name of the application.
        #
        # This value is used in notifications, UI elements, logs, and anywhere
        # the application's name needs to be displayed.
        #--------------------------------------------------------------------------

        name = env('APP_NAME', 'Orionis'),

        #--------------------------------------------------------------------------
        # Debug Mode
        #--------------------------------------------------------------------------
        # Enables or disables detailed error reporting.
        #
        # When set to True, the application will display detailed error messages,
        # which is useful during development but should be disabled in production.
        #--------------------------------------------------------------------------

        debug = env('APP_DEBUG', False),

        #--------------------------------------------------------------------------
        # Bytecode Compilation
        #--------------------------------------------------------------------------
        # Controls whether the application generates bytecode files (.pyc).
        #
        # Setting this to False can be useful in development environments where
        # you do not want bytecode files cluttering the project directory.
        #--------------------------------------------------------------------------

        bytecode = env('APP_BYTECODE', True),

        #--------------------------------------------------------------------------
        # Timezone Configuration
        #--------------------------------------------------------------------------
        # Defines the application's default timezone.
        #
        # This setting ensures consistency when handling timestamps, logs,
        # and scheduled tasks. The default value is 'UTC'.
        #--------------------------------------------------------------------------

        timezone = env('APP_TIMEZONE', 'UTC'),

        #--------------------------------------------------------------------------
        # Uvicorn Server Configuration
        #--------------------------------------------------------------------------
        # Defines the settings for running the application with Uvicorn.
        #
        # - `url`     : The host address for the application.
        # - `port`    : The port number on which the application will run.
        # - `workers` : Number of worker processes to handle requests.
        # - `reload`  : Enables auto-reloading when code changes (useful for development).
        #--------------------------------------------------------------------------

        url = env('APP_URL', '127.0.0.1'),
        port = env('APP_PORT', 8080),
        workers = env('APP_WORKERS', 1),
        reload = env('APP_RELOAD', False),

        #--------------------------------------------------------------------------
        # Application Encryption
        #--------------------------------------------------------------------------
        # Defines the encryption method and key used by the framework.
        #
        # The encryption method used is AES-256-GCM, which ensures secure data
        # encryption. The key should be properly set via environment variables.
        # Supported key sizes: 128, 192, or 256-bit.
        #--------------------------------------------------------------------------

        cipher = 'AES-256-GCM',
        key = env('APP_KEY'),

        #--------------------------------------------------------------------------
        # Additional Values
        #--------------------------------------------------------------------------
        # If your application requires additional configurations, you can define
        # them in this dictionary.
        #--------------------------------------------------------------------------

        custom = {}
    )
