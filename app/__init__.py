from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
app.config.from_object(Config)

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Importar modelos (ESTO FALTA)
from app.models import user_model

from app.controllers import main_controller
