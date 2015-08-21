import os 
from .default_settings import *

try:
    from .local_settings import *
except ImportError:
    pass

_env_settings = os.environ.get('SALTPAD_SETTINGS_MODULE') 
if _env_settings is not None:
    globals().update(
        __import__(
            _env_settings,
            {},
            {}
        ).__dict__
    )
