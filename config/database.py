from flaskavel.luminate.config.dataclass.database import Database, Connections, Sqlite, Mysql, Pgsql, Oracle
from flaskavel.luminate.contracts.config.config_interface import IConfig
from flaskavel.lab.beaker.paths.helpers import database_path
from flaskavel.luminate.bootstrap.register import register
from flaskavel.lab.atomic.environment import env

@register.config
class Config(IConfig):

    config = Database(

        #--------------------------------------------------------------------------
        # Default Database Connection Name
        #--------------------------------------------------------------------------
        # This value defines the default database connection to be used by your
        # application. It can be set to any of the connections defined below.
        #--------------------------------------------------------------------------

        default = env('DB_CONNECTION', 'sqlite'),

        #--------------------------------------------------------------------------
        # Database Connections
        #--------------------------------------------------------------------------
        # Here you can define all of the database connections used by your application.
        # You can configure multiple connections for different database systems such
        # as SQLite, MySQL, PostgreSQL, and Oracle.
        #--------------------------------------------------------------------------

        connections = Connections(

            sqlite = Sqlite(
                driver='sqlite',
                url=env('DB_URL'),
                database=env('DB_DATABASE', database_path('database.sqlite')),
                prefix='',
                foreign_key_constraints=env('DB_FOREIGN_KEYS', True),
                busy_timeout=None,
                journal_mode=None,
                synchronous=None
            ),

            mysql = Mysql(
                driver='mysql',
                url=env('DB_URL'),
                host=env('DB_HOST', '127.0.0.1'),
                port=env('DB_PORT', '3306'),
                database=env('DB_DATABASE', 'flaskavel'),
                username=env('DB_USERNAME', 'root'),
                password=env('DB_PASSWORD', ''),
                unix_socket=env('DB_SOCKET', ''),
                charset=env('DB_CHARSET', 'utf8mb4'),
                collation=env('DB_COLLATION', 'utf8mb4_unicode_ci'),
                prefix='',
                prefix_indexes=True,
                strict=True,
                engine=None
            ),

            pgsql = Pgsql(
                driver='pgsql',
                url=env('DB_URL'),
                host=env('DB_HOST', '127.0.0.1'),
                port=env('DB_PORT', '5432'),
                database=env('DB_DATABASE', 'flaskavel'),
                username=env('DB_USERNAME', 'root'),
                password=env('DB_PASSWORD', ''),
                charset=env('DB_CHARSET', 'utf8'),
                prefix='',
                prefix_indexes=True,
                search_path='public',
                sslmode='prefer'
            ),

            oracle = Oracle(
                driver='oracle',
                dsn=env('DB_DSN'),
                host=env('DB_HOST', '127.0.0.1'),
                port=env('DB_PORT', '1521'),
                username=env('DB_USERNAME', 'root'),
                password=env('DB_PASSWORD', ''),
                charset=env('DB_CHARSET', 'utf8'),
                service=env('DB_SERVICE'),
                sid=env('DB_SID')
            )

        )
    )
