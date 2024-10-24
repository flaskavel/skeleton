from flaskavel.lab.atomic.environment import env
from flaskavel.lab.beaker.paths.helpers import bootstrap_path

cache = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # Solo file en el momento
    #--------------------------------------------------------------------------

    'default' : env('CACHE_STORE', 'file'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'store' : {

        'file' : {
            'routes' : bootstrap_path('cache/routes.lab'),
            'config' : bootstrap_path('cache/config.lab'),
        }
    },

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'encrypt' : env('CACHE_ENCRYPT', False),

}