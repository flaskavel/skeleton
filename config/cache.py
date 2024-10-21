cache = {

    #--------------------------------------------------------------------------
    # Default Cache
    #--------------------------------------------------------------------------
    # Value to select the default configuration used to store the application's
    # cache.
    #--------------------------------------------------------------------------

    'default' : env('CACHE_STORE', 'file'),

    #--------------------------------------------------------------------------
    # Cache Options
    #--------------------------------------------------------------------------
    # Options for storing the application's cache, currently only supports 'file',
    # where routes, config, and sessions will be stored.
    #--------------------------------------------------------------------------

    'store' : {

        'file' : {
            'routes' : None,
            'config' : None,
            'session' : None,
        }
    },

    #--------------------------------------------------------------------------
    # Application Encrypt
    #--------------------------------------------------------------------------
    # Value to determine if the cache should be encrypted, useful for providing
    # an additional layer of security.
    #--------------------------------------------------------------------------

    'encrypt' : env('CACHE_ENCRYPT', True)

}
