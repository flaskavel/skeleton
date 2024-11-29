from flaskavel.lab.atomic.environment import env

app = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of the application, useful for notifications,
    # UI elements, or whenever the application's name needs to be displayed.
    #--------------------------------------------------------------------------

    'name' : env('APP_NAME', 'Flaskavel'),

    #--------------------------------------------------------------------------
    # Application Environment
    #--------------------------------------------------------------------------
    # This value determines the "environment" in which the application is
    # running, useful for determining private system configurations, usually
    # set in the ".env" file.
    #--------------------------------------------------------------------------

    'env' : env('APP_ENV', 'production'),

    #--------------------------------------------------------------------------
    # Application Bytecode
    #--------------------------------------------------------------------------
    # This value determines if the application should run by creating bytecode
    # files, useful if you don't want these files in a dev environment.
    #--------------------------------------------------------------------------

    'bytecode' : env('APP_BYTECODE', True),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # Value used to show detailed error information when an error occurs in
    # the application, useful for deciding whether or not to display details.
    #--------------------------------------------------------------------------

    'debug' : bool(env('APP_DEBUG', False)),

    #--------------------------------------------------------------------------
    # Application Timezone
    #--------------------------------------------------------------------------
    # Value used to set the application's timezone, useful if a different
    # timezone is needed.
    #--------------------------------------------------------------------------

    'timezone' : env('APP_TIMEZONE', 'UTC'),

    #--------------------------------------------------------------------------
    # Application Locale
    #--------------------------------------------------------------------------
    # Value used to determine the application's language and the return value
    # of some functions.
    #--------------------------------------------------------------------------

    'locale' : env('APP_LOCALE', 'en'),

    #--------------------------------------------------------------------------
    # Application URL
    #--------------------------------------------------------------------------
    # Value used to determine the application's URL, useful when you need to
    # access the URL anywhere in the framework without accessing the ".env" file.
    #--------------------------------------------------------------------------

    'url' : env('APP_URL', 'http://localhost'),
    'port' : env('APP_PORT', 5000),

    #--------------------------------------------------------------------------
    # Application Encryption
    #--------------------------------------------------------------------------
    # Values used to define the encryption supported by the framework,
    # supporting 128, 192, 256-bit keys.
    #--------------------------------------------------------------------------

    'cipher' : 'AES-256-GCM',

    'key' : env('APP_KEY')
}
