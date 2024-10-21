from flaskavel.lab.atomic.environment import env

mail = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'default' : env('MAIL_MAILER', 'log'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # smtp-log
    #--------------------------------------------------------------------------

    'mailers' : {

        'smtp' : {
            'transport' : 'smtp',
            'url' : env('MAIL_URL'),
            'host' : env('MAIL_HOST', '127.0.0.1'),
            'port' : env('MAIL_PORT', 2525),
            'encryption' : env('MAIL_ENCRYPTION', 'tls'),
            'username' : env('MAIL_USERNAME'),
            'password' : env('MAIL_PASSWORD'),
            'timeout' : None,
        },

        'log' : {
            'transport' : 'log',
            'channel' : env('MAIL_LOG_CHANNEL'),
        },

    },

}