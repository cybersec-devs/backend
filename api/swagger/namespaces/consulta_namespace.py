from flask_restx import Namespace, Resource, fields
from models import paciente, consulta
from repositories.consulta import ConsultaRepository

consultas_ns = Namespace('Consultas', description='Operações relacionadas as consultas pacientes')

# Modelo aninhado (paciente simplificado)
paciente_relacionado_model = consultas_ns.model("PacienteRelacionado", {
    "id": fields.Integer(description="ID do paciente"),
    "nome": fields.String(description="Nome do paciente")
})

# Modelo de entrada
consulta_input_model = consultas_ns.model("ConsultaInput", {
    "data": fields.String(required=True, description="Data da consulta no formato YYYY-MM-DD"),
    "horario": fields.String(required=True, description="Horário da consulta no formato HH:MM"),
    "descricao": fields.String(description="Descrição opcional"),
    "paciente_id": fields.Integer(required=True, description="ID do paciente")
})

# Modelo de saída
consulta_output_model = consultas_ns.model("ConsultaOutput", {
    "id": fields.Integer(description="ID da consulta"),
    "data": fields.String(description="Data da consulta"),
    "horario": fields.String(description="Horário da consulta"),
    "descricao": fields.String(description="Descrição da consulta"),
    "paciente_id": fields.Integer(description="ID do paciente"),
    "paciente": fields.Nested(paciente_relacionado_model)
})

@consultas_ns.route("/")
class ConsultaListResource(Resource):
    @consultas_ns.marshal_list_with(consulta_output_model)
    def get(self):
        """Lista todos as consultas"""
        response, status_code = ConsultaRepository.get_all()
        return response, status_code
    
    @consultas_ns.expect(consulta_input_model)
    @consultas_ns.marshal_with(consulta_output_model, code=201)
    def post(self):
        """Cria uma nova consulta"""
        data = consultas_ns.payload
        data_obj=data['data']
        horario=data['horario']
        descricao=data.get('descricao')
        paciente_id=data['paciente_id']
        
        response, status_code = ConsultaRepository.create(data_obj, horario, descricao, paciente_id)
        
        return response, status_code

@consultas_ns.route("/<int:id_consulta>")   
class ConsultaResource(Resource):
    #@consultas_ns.marshal_with(consulta_output_model)
    def get(self, id_consulta):
        """Obtém uma consulta pelo ID"""
        response, status = ConsultaRepository.get_by_id(id_consulta)
        return response, status

    @consultas_ns.expect(consulta_input_model)
    @consultas_ns.marshal_with(consulta_output_model)
    def put(self, id_consulta):
        """Atualiza uma consulta"""
        data = consultas_ns.payload
        data_obj=data['data']
        horario=data['horario']
        descricao=data.get('descricao')
        
        return ConsultaRepository.update(id_consulta, data_obj, horario, descricao)

    def delete(self, id_consulta):
        """Exclui uma consulta"""
        response, status = ConsultaRepository.delete(id_consulta)
        return response, status