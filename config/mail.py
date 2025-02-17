from orionis.luminate.config.dataclass.mail import Mail, Mailers, Smtp, File
from orionis.luminate.contracts.config.config_interface import IConfig
from orionis.luminate.bootstrap.register import register
from orionis.luminate.facades.paths import storage_path
from orionis.luminate.facades.environment import env

@register.config
class Config(IConfig):

    config = Mail(

        #--------------------------------------------------------------------------
        # Default Mailer
        #--------------------------------------------------------------------------
        # This value defines the default mailer used by the application.
        #--------------------------------------------------------------------------

        default = env('MAIL_MAILER', 'log'),

        #--------------------------------------------------------------------------
        # Mailers Configuration
        #--------------------------------------------------------------------------
        # This section defines the different mailers available for sending emails
        # from the application. You can configure multiple transport methods here,
        # such as SMTP or logging.
        #--------------------------------------------------------------------------

        mailers = Mailers(

            #----------------------------------------------------------------------
            # SMTP _ Mailer
            #----------------------------------------------------------------------
            # Configuration for sending emails via SMTP. This is the most common
            # method for connecting to an external mail server.
            #----------------------------------------------------------------------

            smtp = Smtp(
                url = env('MAIL_URL'),
                host = env('MAIL_HOST'),
                port = env('MAIL_PORT'),
                encryption = env('MAIL_ENCRYPTION'),
                username = env('MAIL_USERNAME'),
                password = env('MAIL_PASSWORD'),
                timeout = None
            ),

            #----------------------------------------------------------------------
            # Log Mailer
            #----------------------------------------------------------------------
            # Configuration for logging emails to the application's logs.
            #----------------------------------------------------------------------
            file = File(
                path=storage_path('mails')
            )

        )
    )