queue = {

    'default' : env('QUEUE_CONNECTION', 'database'),

    'connections': {

        'database' : {
            'driver' : 'database',
            'connection' : env('DB_QUEUE_CONNECTION'),
            'table' : env('DB_QUEUE_TABLE', 'jobs'),
            'batching' : env('DB_QUEUE_BATCHING', 'job_batches'),
            'failed' : env('DB_QUEUE_FAILED', 'job_failures'),
            'queue' : env('DB_QUEUE', 'default'),
            'retry_after' : (int) env('DB_QUEUE_RETRY_AFTER', 90),
            'after_commit' : False,
        }
    },

}