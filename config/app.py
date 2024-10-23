from flaskavel.lab.atomic.environment import env

app = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'name' : env('APP_NAME', 'Flaskavel'),

    #--------------------------------------------------------------------------
    # Application Environment
    #--------------------------------------------------------------------------
    # This value determines the "environment" your application is currently
    # running in. This may determine how you prefer to configure various
    # services the application utilizes. Set this in your ".env" file.
    #--------------------------------------------------------------------------

    'env' : env('APP_ENV', 'production'),

    #--------------------------------------------------------------------------
    # Application Environment
    #--------------------------------------------------------------------------
    # This value determines the "environment" your application is currently
    # running in. This may determine how you prefer to configure various
    # services the application utilizes. Set this in your ".env" file.
    #--------------------------------------------------------------------------

    'bytecode' : bool(env('APP_BYTECODE', True)),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    #--------------------------------------------------------------------------

    'debug' : bool(env('APP_DEBUG', False)),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    #--------------------------------------------------------------------------

    'timezone' : env('APP_TIMEZONE', 'UTC'),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    #--------------------------------------------------------------------------

    'locale' : env('APP_LOCALE', 'en'),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    #--------------------------------------------------------------------------

    'url' : env('APP_URL', 'http://localhost'),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    #--------------------------------------------------------------------------

    'cipher' : 'AES-192-GCM',

    'key' : env('APP_KEY'),

    #--------------------------------------------------------------------------
    # Application Debug Mode
    #--------------------------------------------------------------------------
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    #--------------------------------------------------------------------------

    'url' : env('APP_URL', 'http://localhost'),

}