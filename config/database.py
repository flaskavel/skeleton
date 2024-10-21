database = {

    #--------------------------------------------------------------------------
    # Default Database Connection Name
    #--------------------------------------------------------------------------
    # This value defines the default database connection to be used by your
    # application. It can be set to any of the connections defined below.
    #--------------------------------------------------------------------------

    'default' : env('DB_CONNECTION', 'sqlite'),

    #--------------------------------------------------------------------------
    # Database Connections
    #--------------------------------------------------------------------------
    # Here you can define all of the database connections used by your application.
    # You can configure multiple connections for different database systems such
    # as SQLite, MySQL, PostgreSQL, and Oracle.
    #--------------------------------------------------------------------------
    
    'connections': {
        
        #----------------------------------------------------------------------
        # SQLite Connection
        #----------------------------------------------------------------------
        # This configuration is for using an SQLite database. It is a lightweight
        # and easy-to-use database engine that stores data in a single file.
        # SQLite is ideal for small projects or testing environments.
        #----------------------------------------------------------------------
        
        'sqlite' : {
            'driver' : 'sqlite',
            'url' : env('DB_URL'),
            'database' : env('DB_DATABASE', database_path('database.sqlite')),
            'prefix' : '',
            'foreign_key_constraints' : env('DB_FOREIGN_KEYS', True),
            'busy_timeout' : None,
            'journal_mode' : None,
            'synchronous' : None,
        },

        #----------------------------------------------------------------------
        # MySQL Connection
        #----------------------------------------------------------------------
        # This configuration is for using a MySQL database. MySQL is a popular
        # relational database management system known for its scalability and
        # performance. You can configure the connection with host, port, and other
        # options as defined below.
        #----------------------------------------------------------------------
        
        'mysql' : {
            'driver' : 'mysql',
            'url' : env('DB_URL'),
            'host' : env('DB_HOST', '127.0.0.1'),
            'port' : env('DB_PORT', '3306'),
            'database' : env('DB_DATABASE', 'flaskavel'),
            'username' : env('DB_USERNAME', 'root'),
            'password' : env('DB_PASSWORD', ''),
            'unix_socket' : env('DB_SOCKET', ''),
            'charset' : env('DB_CHARSET', 'utf8mb4'),
            'collation' : env('DB_COLLATION', 'utf8mb4_unicode_ci'),
            'prefix' : '',
            'prefix_indexes' : True,
            'strict' : True,
            'engine' : None,
        },

        #----------------------------------------------------------------------
        # PostgreSQL Connection
        #----------------------------------------------------------------------
        # This configuration is for using a PostgreSQL database. PostgreSQL is an
        # advanced object-relational database system known for its robustness and
        # support for complex queries and large datasets.
        #----------------------------------------------------------------------

        'pgsql' : {
            'driver' : 'pgsql',
            'url' : env('DB_URL'),
            'host' : env('DB_HOST', '127.0.0.1'),
            'port' : env('DB_PORT', '5432'),
            'database' : env('DB_DATABASE', 'flaskavel'),
            'username' : env('DB_USERNAME', 'root'),
            'password' : env('DB_PASSWORD', ''),
            'charset' : env('DB_CHARSET', 'utf8'),
            'prefix' : '',
            'prefix_indexes' : True,
            'search_path' : 'public',
            'sslmode' : 'prefer',
        },

        #----------------------------------------------------------------------
        # Oracle Connection
        #----------------------------------------------------------------------
        # This configuration is for using an Oracle database. Oracle is a highly
        # scalable and widely used enterprise-level relational database system.
        # You can configure the connection using the DSN (Data Source Name) along
        # with other environment variables such as host, port, and service name.
        #----------------------------------------------------------------------

        'oracle': {
            'driver' : 'oracle',
            'dsn' : env('DB_DSN'),
            'host' : env('DB_HOST', '127.0.0.1'),
            'port' : env('DB_PORT', '1521'),
            'username' : env('DB_USERNAME', 'root'),
            'password' : env('DB_PASSWORD', ''),
            'charset' : env('DB_CHARSET', 'utf8'),
            'service' : env('DB_SERVICE'),
            'sid' : env('DB_SID'),
        }
    }
}
