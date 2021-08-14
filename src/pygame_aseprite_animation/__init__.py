import logging
from pygame_aseprite_animation import *

logger = logging.getLogger(__name__)

try:
    import py_aseprite
except ImportError:
    logger.debug('cannot import py_aseprite')

__version__ = (0, 0, 1)
__author__ = 'Besmir Sejdijaj'
__author_email__ = 'b.sejdijaj@hotmail.com'
__description__ = 'Import and handle aseprite files in pygame'