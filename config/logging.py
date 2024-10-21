from flaskavel.lab.atomic.environment import env
from flaskavel.lab.beaker.paths.helpers import storage_path

logging = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'default' : env('LOG_CHANNEL', 'stack'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------
    'channels' : {

        'stack' : {
            'driver' : 'stack',
            'path' : storage_path('logs/flaskavel.log'),
            'ignore_exceptions' : False,
        },

        'single' : {
            'driver' : 'single',
            'path' : storage_path('logs/flaskavel.log'),
            'level' : env('LOG_LEVEL', 'debug'),
            'replace_placeholders' : True,
        },

        'daily' : {
            'driver' : 'daily',
            'path' : storage_path('logs/flaskavel.log'),
            'level' : env('LOG_LEVEL', 'debug'),
            'days' : env('LOG_DAILY_DAYS', 14),
            'replace_placeholders' : True,
        },
    }
}