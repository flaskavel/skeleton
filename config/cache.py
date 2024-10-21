cache = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # Solo file en el momento
    #--------------------------------------------------------------------------

    'default' : env('CACHE_STORE', 'file'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'store' : {

        'file' : {
            'routes' : None,
            'config' : None,
            'session' : None,
        }
    },

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'encrypt' : env('CACHE_ENCRYPT', True)

}