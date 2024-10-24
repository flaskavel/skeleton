from flaskavel.lab.atomic.environment import env
from flaskavel.lab.beaker.paths.helpers import storage_path

filesystems = {

    #--------------------------------------------------------------------------
    # Default File System Disk
    #--------------------------------------------------------------------------
    # This value defines the default file storage configuration to be used
    # in the application.
    #--------------------------------------------------------------------------

    'default' : env('FILESYSTEM_DISK', 'local'),

    #--------------------------------------------------------------------------
    # File System Disks
    #--------------------------------------------------------------------------
    # Configuration for each of the storage options that can be used in the system.
    # Here, you can define multiple disks for storing files locally or on cloud services
    # like Amazon S3.
    #--------------------------------------------------------------------------
    
    'disks' : {

        #----------------------------------------------------------------------
        # Local Disk
        #----------------------------------------------------------------------
        # Configuration for storing files locally on the server's file system.
        # Useful for private files or internal data storage.
        #----------------------------------------------------------------------

        'local' : {
            'driver' : 'local',
            'root' : storage_path('app/private'),
            'serve' : True,
            'throw' : False,
        },

        #----------------------------------------------------------------------
        # Public Disk
        #----------------------------------------------------------------------
        # Configuration for storing publicly accessible files. Files stored here
        # will be available through a public URL.
        #----------------------------------------------------------------------

        'public' : {
            'driver' : 'local',
            'root' : storage_path('app/public'),
            'url' : env('APP_URL') + '/storage',
            'visibility' : 'public',
            'throw' : False,
        },

        #----------------------------------------------------------------------
        # Amazon S3 Disk
        #----------------------------------------------------------------------
        # Configuration for using Amazon S3 to store files in the cloud. S3 is a
        # popular, scalable cloud storage service. You can configure the access
        # credentials, bucket name, and other options here.
        #----------------------------------------------------------------------

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