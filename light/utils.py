import logging
import pathlib
from importlib import import_module


_LOG_PREFIX = '[SETTINGS-IMPORTER]'
_PROJECT_SETTINGS = 'settings'


logger = logging.getLogger(__name__)

def _get_project_settings():
    path = pathlib.Path('settings.py')
    if path.is_file():
        return path.parent.name
    return pathlib.Path('light/settings.py').parent.name



def import_settings():
    path = _get_project_settings()
    logger.debug(f'{_LOG_PREFIX} Importing settings from {path}')
    try:
        return import_module(_PROJECT_SETTINGS)
    except ModuleNotFoundError:
        logger.warning('You should create your own settings.py file!')
        return import_module(f'{path}.{_PROJECT_SETTINGS}')
