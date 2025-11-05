from flask import Flask
from dotenv import load_dotenv
import os
from .models import db 
from .routes import bp as api_bp
from .ui_routes import bp_ui 

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")

    if not db_uri:
        raise RuntimeError("Variável de ambiente 'SQLALCHEMY_DATABASE_URI' não encontrada. Verifique o .env e o Docker.")

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy
    db.init_app(app)

    # Registra o Blueprint da API (para /tasks)
    app.register_blueprint(api_bp)
    # Registra o Blueprint da UI (para /)
    app.register_blueprint(bp_ui)

    with app.app_context():
        from .models import Task 
        db.create_all()

    return app
