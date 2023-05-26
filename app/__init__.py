from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

# Instantiate a flsk object
app = Flask(__name__)

# Access ennvironment variables available through a flask context
app.config.from_object(Config)

# Instantiate packages used
bootstrap = Bootstrap(app)

# From a flask context, import other modules found in the app subfolder
# Imported at the bottom to avoid circular dependancies
from app import routes, errors
