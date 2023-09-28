from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.usuario_bp import usuario_bp
from .routes.servidor_bp import servidor_bp
from .routes.canal_bp import canal_bp
from .routes.chat_bp import chat_bp
from .database import DatabaseConnection


def init_app():
    """Crea y configura la aplicacion de Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    CORS(app, supports_credentials=True)
    
    app.config.from_object(
        Config
    )
    app.register_blueprint(usuario_bp, url_prefix = '/usuarios')
    app.register_blueprint(servidor_bp, url_prefix='/servidores')
    app.register_blueprint(canal_bp, url_prefix='/canales')
    app.register_blueprint(chat_bp, url_prefix= '/chat')
    
    DatabaseConnection.set_config(app.config)
    
    
    @app.route('/')
    def inicio():
        return 'Bienvenidos'
    
    return app