from decouple import config
import json
from swagger.swagger_config import configure_swagger
from config import Config, db
from flask import Flask
from flask_cors import CORS
from controllers.medico import medico_bp
from controllers.paciente import paciente_bp
from controllers.consulta import consulta_bp
from controllers.medico import get_all_medicos
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config)      # <-- primeiro aplica a configuração
db.init_app(app)                    # <-- depois inicializa o SQLAlchemy

CORS(app)
# Registra blueprints
app.register_blueprint(medico_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(consulta_bp)

# Cria as tabelas
with app.app_context():
    db.create_all()

# Swagger
configure_swagger(app)

if __name__ == '__main__':
   app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])