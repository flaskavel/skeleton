from flaskavel.luminate.contracts.config.config_interface import IConfig
from flaskavel.luminate.config.dataclass.cache import Data
from flaskavel.luminate.facades.paths import storage_path
from flaskavel.luminate.facades.environment import env

class Cache(IConfig):

    config = Data(

        #--------------------------------------------------------------------------
        # Default Cache
        #--------------------------------------------------------------------------
        # Value to select the default configuration used to store the application's
        # cache.
        #--------------------------------------------------------------------------

        default = env('CACHE_STORE', None),

        #--------------------------------------------------------------------------
        # Cache Options
        #--------------------------------------------------------------------------
        # Options for storing the application's cache, currently only supports 'file',
        # where routes, config, and sessions will be stored.
        #--------------------------------------------------------------------------

        stores = {
            'file' : {
                'path' : storage_path('framework/cache/data')
            },
        },
    )
