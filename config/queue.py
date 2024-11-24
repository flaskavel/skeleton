from flaskavel.lab.atomic.environment import env

queue = {

    #--------------------------------------------------------------------------
    # Default Queue Connection
    #--------------------------------------------------------------------------
    # This value defines the default connection to be used for the queue system.
    #--------------------------------------------------------------------------

    'default' : env('QUEUE_CONNECTION', 'database'),

    #--------------------------------------------------------------------------
    # Queue Connections Configuration
    #--------------------------------------------------------------------------
    # This section defines the different connections available for the queue system.
    #--------------------------------------------------------------------------

    'connections': {

        #----------------------------------------------------------------------
        # Database Queue Connection.
        #----------------------------------------------------------------------
        # Configuration for using the database as the queue driver. This allows
        # queue to be stored in a database table and processed in the background.
        #----------------------------------------------------------------------

        'database' : {
            'driver' : 'database',
            'connection' : env('DB_QUEUE_CONNECTION'),
            'table' : env('DB_QUEUE_TABLE', 'jobs'),
            'batching' : env('DB_QUEUE_BATCHING', 'job_batches'),
            'failed' : env('DB_QUEUE_FAILED', 'job_failures'),
            'queue' : env('DB_QUEUE', 'default'),
            'retry_after' : int(env('DB_QUEUE_RETRY_AFTER', 90)),
            'after_commit' : False,
        }
    },

}