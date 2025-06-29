from flask_restx import Namespace, Resource, fields
from models import medico
from repositories.medico import get_medicos, create_medico, get_medico_by_id, update_medico, delete_medico

medicos_ns = Namespace("Médicos", description="Operações relacionadas aos médicos")

medico_model = medicos_ns.model("Medico", {
    "nome": fields.String(required=True, description="Nome do medico"),
    "especialidade": fields.String(required=True, description="Área de especialidade"),
    "crm": fields.String(required=True, description="CRM")
})

medico_output_model = medicos_ns.model("MedicoOutput", {
    "id": fields.Integer(description="ID do medico"),
    "nome": fields.String(required=True, description="Nome do medico"),
    "especialidade": fields.String(required=True, description="Área de especialidade"),
    "crm": fields.String(required=True, description="Número do CRM")
})

@medicos_ns.route("/")
class MedicosResource(Resource):
    @medicos_ns.marshal_list_with(medico_output_model)
    def get(self):
        """Lista todos os médicos"""
        return get_medicos()

    @medicos_ns.expect(medico_model)
    def post(self):
        """Cria um novo médico"""
        data = medicos_ns.payload
        nome = data['nome']
        especialidade = data['especialidade']
        crm = data['crm']
        response, status_code = create_medico(nome, especialidade, crm)
        
        return response, status_code

@medicos_ns.route("/<int:id_medico>")
class MedicoIdResource(Resource):
    def get(self, id_medico):
        """Obtém um médico pelo ID"""
        response, status_code = get_medico_by_id(id_medico)
        return response, status_code    

    @medicos_ns.expect(medico_model)
    def put(self, id_medico):
        """Atualiza um médico pelo ID"""
        data = medicos_ns.payload
        nome = data['nome']
        especialidade = data['especialidade']
        crm = data['crm']
        response, status_code = update_medico(id_medico,nome, especialidade, crm)        
        return response, status_code

    def delete(self, id_medico):
        """Exclui um médico pelo ID"""
        response, status_code = delete_medico(id_medico)
        return response, status_code
