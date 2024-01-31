from flask import render_template, Blueprint
from .xbox.generator_config import *

blue = Blueprint(
    BLUEPRINT_NAME, 
    __name__, 
    url_prefix = URL_PREFIX,
    template_folder = TEMPLATE_FOLDER,
    static_folder = STATIC_FOLDER,
    static_url_path = STATIC_URL_PATH,
)


@blue.route('/')
def index():
    return render_template(f'index.html')