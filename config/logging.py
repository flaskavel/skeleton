from orionis.luminate.config.dataclass.logging import Logging, Channels, Single, Daily, Chunked
from orionis.luminate.contracts.config.config_interface import IConfig
from orionis.luminate.bootstrap.register import register
from orionis.luminate.facades.paths import storage_path
from orionis.luminate.facades.environment import env

@register.config
class Config(IConfig):

    config = Logging(

        #--------------------------------------------------------------------------
        # Default Logging Configuration
        #--------------------------------------------------------------------------
        # This value defines the default logging configuration used by the application.
        #--------------------------------------------------------------------------

        default = env('LOG_CHANNEL', 'stack'),

        #--------------------------------------------------------------------------
        # Logging Channels
        #--------------------------------------------------------------------------
        # Here you can configure the different logging channels used by the application.
        # Each channel represents a way to write logs to a different location such as
        # a file, the console, or an external service.
        #--------------------------------------------------------------------------

        channels = Channels(

            #----------------------------------------------------------------------
            # Single File Channel
            #----------------------------------------------------------------------
            # This channel writes all log entries to a single log file. Useful for
            # applications that do not require rotation or segmentation of log files.
            #----------------------------------------------------------------------

            single = Single(
                path=storage_path('logs/orionis.log'),
                level=env('LOG_LEVEL', 'debug'),
                stream=False
            ),

            #----------------------------------------------------------------------
            # Daily Log Channel
            #----------------------------------------------------------------------
            # This channel writes log entries to a new file every day. It is useful for
            # rotating log files, especially when you want to keep logs separated by
            # day and automatically clean up old files after a specified number of days.
            #----------------------------------------------------------------------

            daily = Daily(
                path=storage_path('logs/orionis.log'),
                level=env('LOG_LEVEL', 'debug'),
                days=env('LOG_DAILY_DAYS', 14),
                stream=False
            ),

            #----------------------------------------------------------------------
            # Chunked Log Channel
            #----------------------------------------------------------------------
            # This channel writes log entries to a series of files, each of which is
            # a maximum size. When the log file reaches the maximum size, a new file
            # is created. This is useful for applications that generate large log files.
            #----------------------------------------------------------------------

            chunked = Chunked(
                path=storage_path('logs/orionis.log'),
                level=env('LOG_LEVEL', 'debug'),
                max_size=env('LOG_CHUNKED_SIZE', 1000000),
                max_files=env('LOG_CHUNKED_FILES', 5),
                stream=False
            )

        )
    )