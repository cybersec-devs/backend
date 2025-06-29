
from . import api
from swagger.namespaces.medico_namespace import medicos_ns
from swagger.namespaces.paciente_namespace import pacientes_ns
from swagger.namespaces.consulta_namespace import consultas_ns

# Função para registrar os namespaces
def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(medicos_ns, path="/medicos")
    api.add_namespace(pacientes_ns, path="/pacientes")
    api.add_namespace(consultas_ns, path="/consultas")
    api.mask_swagger = False