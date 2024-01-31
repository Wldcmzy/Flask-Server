from .blueprint import blue
from .xbox.generator_config import MODULE_NAME, URL_PREFIX
from ..master.appfile import app, active_modules, ModuleMessage
app.register_blueprint(blue)
active_modules.append(ModuleMessage(MODULE_NAME, URL_PREFIX))