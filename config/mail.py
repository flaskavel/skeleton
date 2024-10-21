main = {

    #--------------------------------------------------------------------------
    # Default Mailer
    #--------------------------------------------------------------------------
    # This value defines the default mailer used by the application.
    #--------------------------------------------------------------------------

    'default' : env('MAIL_MAILER', 'log'),

    #--------------------------------------------------------------------------
    # Mailers Configuration
    #--------------------------------------------------------------------------
    # This section defines the different mailers available for sending emails
    # from the application. You can configure multiple transport methods here,
    # such as SMTP or logging.
    #--------------------------------------------------------------------------

    'mailers' : {

        #----------------------------------------------------------------------
        # SMTP Mailer
        #----------------------------------------------------------------------
        # Configuration for sending emails via SMTP. This is the most common
        # method for connecting to an external mail server.
        #----------------------------------------------------------------------

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

        #----------------------------------------------------------------------
        # Log Mailer
        #----------------------------------------------------------------------
        # Configuration for logging emails instead of sending them. This is
        # useful for debugging, allowing you to view the email content without
        # actually sending it.
        #----------------------------------------------------------------------

        'log' : {
            'transport' : 'log',
            'channel' : env('MAIL_LOG_CHANNEL'),
        },

    },

}
