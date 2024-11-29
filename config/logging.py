from flaskavel.lab.atomic.environment import env
from flaskavel.lab.beaker.paths.helpers import storage_path

logging = {

    #--------------------------------------------------------------------------
    # Default Logging Configuration
    #--------------------------------------------------------------------------
    # This value defines the default logging configuration used by the application.
    #--------------------------------------------------------------------------

    'default' : env('LOG_CHANNEL', 'stack'),

    #--------------------------------------------------------------------------
    # Logging Channels
    #--------------------------------------------------------------------------
    # Here you can configure the different logging channels used by the application.
    # Each channel represents a way to write logs to a different location such as
    # a file, the console, or an external service.
    #--------------------------------------------------------------------------

    'channels' : {

        #----------------------------------------------------------------------
        # Stack Channel
        #----------------------------------------------------------------------
        # This logging channel allows logs to be sent to multiple channels
        # at the same time. Logs can be stacked and written to several files
        # or services.
        #----------------------------------------------------------------------

        'stack' : {
            'driver' : 'stack',
            'path' : storage_path('logs/flaskavel.log'),
            'ignore_exceptions' : False,
        },

        #----------------------------------------------------------------------
        # Single File Channel
        #----------------------------------------------------------------------
        # This channel writes all log entries to a single log file. Useful for
        # applications that do not require rotation or segmentation of log files.
        #----------------------------------------------------------------------

        'single' : {
            'driver' : 'single',
            'path' : storage_path('logs/flaskavel.log'),
            'level' : env('LOG_LEVEL', 'debug'),
            'replace_placeholders' : True,
        },

        #----------------------------------------------------------------------
        # Daily Log Channel
        #----------------------------------------------------------------------
        # This channel writes log entries to a new file every day. It is useful for
        # rotating log files, especially when you want to keep logs separated by
        # day and automatically clean up old files after a specified number of days.
        #----------------------------------------------------------------------

        'daily' : {
            'driver' : 'daily',
            'path' : storage_path('logs/flaskavel.log'),
            'level' : env('LOG_LEVEL', 'debug'),
            'days' : env('LOG_DAILY_DAYS', 14),
            'replace_placeholders' : True,
        },
    }
}