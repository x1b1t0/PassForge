from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    from userModel import User
    from passwordController import password_bp
    from authMiddleware import token_required

    # Registrar Blueprints
    app.register_blueprint(password_bp, url_prefix='/api')

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app