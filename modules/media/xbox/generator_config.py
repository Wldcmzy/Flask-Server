import re

MODULE_NAME = '格林剧团'

BLUEPRINT_NAME = 'media'
URL_PREFIX = '/media'
TEMPLATE_FOLDER = 'templates'
STATIC_FOLDER = 'static'
STATIC_URL_PATH = '/resourcemedia'

CONTENT_FOLDER = 'content'
WEBPAGE_FOLDER = 'webpage'



DEFAULT_IMAGE_1_URL = '/media/resourcemedia/img/default.png'

EODFSP_FILE_NAME = '_EODFSP.json'
INDEX_FILE_NAME = 'index.html'
IMAGE_FILE_FORMAT_LIST: list[str] = (
    'jpg',
    'png',
    'bmp',
    'webp',
)
IMAGE_PREVIEW_FILE_NAME_LIST: list[str] = [f'_image_preview.{f}' for f in IMAGE_FILE_FORMAT_LIST]
COVER_FILE_NAME_LIST: list[str] = [f'_cover.{f}' for f in IMAGE_FILE_FORMAT_LIST]
MUSIC_FILE_FORMA_LIST: list[str] = (
    'mp3', 
)


IMAGESET_NAME_REPLACE_PATTERN_LIST = (
    re.compile(r'^capture\d+'),
)


VIDEO_CAPTIONS_FOLDER = '_captions'
VIDEO_CAPTIONS_MAP_FILE = '_map.json'


