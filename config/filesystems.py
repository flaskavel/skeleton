from flaskavel.lab.atomic.environment import env
from flaskavel.lab.beaker.paths.helpers import storage_path

filesystems = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------
    'default' : env('FILESYSTEM_DISK', 'local'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------
    'disks' : {

        'local' : {
            'driver' : 'local',
            'root' : storage_path('app/private'),
            'serve' : True,
            'throw' : False,
        },

        'public' : {
            'driver' : 'local',
            'root' : storage_path('app/public'),
            'url' : env('APP_URL') + '/storage',
            'visibility' : 'public',
            'throw' : False,
        },

        's3' : {
            'driver' : 's3',
            'key' : env('AWS_ACCESS_KEY_ID'),
            'secret' : env('AWS_SECRET_ACCESS_KEY'),
            'region' : env('AWS_DEFAULT_REGION'),
            'bucket' : env('AWS_BUCKET'),
            'url' : env('AWS_URL'),
            'endpoint' : env('AWS_ENDPOINT'),
            'use_path_style_endpoint' : env('AWS_USE_PATH_STYLE_ENDPOINT', False),
            'throw' : False,
        },

    },
}