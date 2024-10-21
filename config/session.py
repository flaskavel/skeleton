session = {

    #--------------------------------------------------------------------------
    # Session Driver
    #--------------------------------------------------------------------------
    # This value defines the driver to be used for session management.
    #--------------------------------------------------------------------------

    'driver' : env('SESSION_DRIVER', 'file'),

    #--------------------------------------------------------------------------
    # Session Lifetime
    #--------------------------------------------------------------------------
    # This value sets the duration (in minutes) for how long the session
    # will be valid before it expires.
    #--------------------------------------------------------------------------

    'lifetime' : env('SESSION_LIFETIME', 120),

    #--------------------------------------------------------------------------
    # Expire on Close
    #--------------------------------------------------------------------------
    # This value determines whether the session should expire when the user
    # closes their browser. If set to True, the session will not persist
    # after the browser is closed.
    #--------------------------------------------------------------------------

    'expire_on_close' : env('SESSION_EXPIRE_ON_CLOSE', False),

    #--------------------------------------------------------------------------
    # Session Encryption
    #--------------------------------------------------------------------------
    # This value specifies whether the session data should be encrypted
    # for additional security. If set to True, the session will be encrypted.
    #--------------------------------------------------------------------------

    'encrypt' : env('SESSION_ENCRYPT', False),

    #--------------------------------------------------------------------------
    # Session File Path
    #--------------------------------------------------------------------------
    # This value defines the directory path where session files will be stored
    # when using the file driver.
    #--------------------------------------------------------------------------

    'files' : storage_path('framework/sessions'),

    #--------------------------------------------------------------------------
    # Session Cookie Configuration
    #--------------------------------------------------------------------------
    # This section configures the properties of the session cookie.
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
