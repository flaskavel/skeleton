session = {

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------
    'driver' : env('SESSION_DRIVER', 'file'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------
    'lifetime' : env('SESSION_LIFETIME', 120),

    'expire_on_close' : env('SESSION_EXPIRE_ON_CLOSE', False),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'encrypt' : env('SESSION_ENCRYPT', False),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'files' : storage_path('framework/sessions'),

    #--------------------------------------------------------------------------
    # Application Name
    #--------------------------------------------------------------------------
    # This value is the name of your application, which will be used when the
    # framework needs to place the application's name in a notification or
    # other UI elements where an application name needs to be displayed.
    #--------------------------------------------------------------------------

    'cookie' : {
        'name' : env('SESSION_COOKIE', f"{str(env('APP_NAME', 'flaskavel')).lower()}_session"),
        'path' : env('SESSION_PATH', '/'),
        'domain' : env('SESSION_DOMAIN'),
        'secure' : env('SESSION_SECURE_COOKIE'),
        'http_only' : env('SESSION_HTTP_ONLY', True),
        'same_site' : env('SESSION_SAME_SITE', 'lax'),
    }

}