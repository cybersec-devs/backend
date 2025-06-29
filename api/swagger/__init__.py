from flask_restx import Api

# Inicializa o objeto API do Swagger

api = Api(
    title="Hospital Web System API",
    version="1.0",
    description="Documentação da API com Swagger via Flask-RESTX",
    doc="/",  # caminho onde a UI do Swagger será acessada
    mask_swagger=False,  # Desativa o X-Fields no Swagger,
    prefix="/api"
)
