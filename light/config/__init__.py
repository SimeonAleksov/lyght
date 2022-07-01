import os
from importlib import import_module


from light.config import global_settings
from light.routes import Routes
from light.config.exceptions import ImproperlyRouteConfigurationError


empty = object()
ENVIRONMENT_SETTINGS_VARIABLE = 'LIGHT_SETTINGS'
_DEFAULT_ROUTE_CONFIG_MODULE_NAME = 'ROUTE_CONF_MODULE'


class Settings:
    def __init__(self, settings_module):
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(global_settings, setting))

        self.SETTINGS_MODULE = settings_module
        module = import_module(self.SETTINGS_MODULE)
        self._explicit_settings = set()
        for setting in dir(module):
            if setting.isupper():
                setting_value = getattr(module, setting)
                if setting_value == _DEFAULT_ROUTE_CONFIG_MODULE_NAME:
                    routes_module = import_module(setting_value)
                    print(routes_module)
                    routes = getattr(routes_module, 'route_config')
                    if not isinstance(routes, Routes):
                        raise ImproperlyRouteConfigurationError(
                            'The provided module for routes has invalid configured routes. Make sure it points to light.routes.Routes.'
                        )

                    setattr(self, 'ROUTES', routes)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)


class LazySettings:
    def __init__(self):
        st_module = os.environ.get(ENVIRONMENT_SETTINGS_VARIABLE)
        self._settings = Settings(st_module)

    def __getattr__(self, name):
        if (_settings := self._settings) is empty:
            self._setup(name)
            _settings = self._wrapped
        val = getattr(_settings, name)
        self.__dict__[name] = val
        return val


settings = LazySettings()
