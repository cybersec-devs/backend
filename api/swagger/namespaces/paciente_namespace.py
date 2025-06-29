from flask_restx import Namespace, Resource, fields
from models import paciente
from repositories.paciente import PacienteRepository

pacientes_ns = Namespace('Pacientes', description='Operações relacionadas aos pacientes')


# Modelo de entrada (para POST e PUT)
paciente_model = pacientes_ns.model("PacienteInput", {
    "nome": fields.String(required=True, description="Nome do paciente"),
    "medico_id": fields.Integer(required=True, description="ID do médico responsável")
})

# Modelo aninhado: médico associado ao paciente
medico_relacionado_model = pacientes_ns.model("MedicoRelacionado", {
    "id": fields.Integer(description="ID do médico"),
    "nome": fields.String(description="Nome do médico"),
    "crm": fields.String(description="CRM do médico"),
    "especialidade": fields.String(description="Especialidade médica")
})

# Modelo de saída
paciente_output_model = pacientes_ns.model("PacienteOutput", {
    "id": fields.Integer(description="ID do paciente"),
    "nome": fields.String(description="Nome do paciente"),
    "medico_id": fields.Integer(description="ID do médico"),
    "medico": fields.Nested(medico_relacionado_model)
})

@pacientes_ns.route("/")
class PacienteListResource(Resource):
    @pacientes_ns.marshal_list_with(paciente_output_model)
    def get(self):
        """Lista todos os pacientes"""
        response, status_code = PacienteRepository.get_all()
        return response, status_code
    
    @pacientes_ns.expect(paciente_model)
    def post(self):
        """Cria um novo paciente"""
        data = pacientes_ns.payload
        nome = data['nome']
        medico_id = data['medico_id']
        response, status_code = PacienteRepository.create(nome, medico_id)
        
        return response, status_code

@pacientes_ns.route("/<int:id_paciente>")   
class PacienteResource(Resource):
    #@pacientes_ns.marshal_with(paciente_output_model)
    def get(self, id_paciente):
        """Obtém um paciente pelo ID"""
        response, status = PacienteRepository.get_by_id(id_paciente)
        return response, status

    @pacientes_ns.expect(paciente_model)
    @pacientes_ns.marshal_with(paciente_output_model)
    def put(self, id_paciente):
        """Atualiza um paciente"""
        data = pacientes_ns.payload
        return PacienteRepository.update(id_paciente, data['nome'], data['medico_id'])

    def delete(self, id_paciente):
        """Exclui um paciente"""
        response, status = PacienteRepository.delete(id_paciente)
        return response, status