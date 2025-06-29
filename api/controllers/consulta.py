from flask import Blueprint, request, jsonify
from repositories.consulta import ConsultaRepository
from datetime import datetime

consulta_bp = Blueprint('consulta', __name__,url_prefix='/consultas')

@consulta_bp.route('', methods=['POST'])
def create_consulta():
    data = request.get_json()
    data_date = datetime.strptime(data['data'], '%Y-%m-%d').date()
    horario_time = datetime.strptime(data['horario'], '%H:%M').time()
    consulta = ConsultaRepository.create(data_date, horario_time, data.get('descricao'), data['paciente_id'])
    return jsonify(consulta.to_dict()), 201    
    

@consulta_bp.route('', methods=['GET'])
def get_consultas():
    response, status = ConsultaRepository.get_all()
    return jsonify(response), status

@consulta_bp.route('/<int:consulta_id>', methods=['GET'])
def get_consulta(consulta_id):
    consulta, status = ConsultaRepository.get_by_id(consulta_id)
    if consulta:
        return jsonify(consulta), status
    return jsonify({'error': 'Consulta não encontrada'}), 404


@consulta_bp.route('/pacientes/<int:paciente_id>/consultas', methods=['GET'])
def get_consultas_by_paciente(paciente_id):
    consultas = ConsultaRepository.get_by_paciente(paciente_id)
    return jsonify([c.to_dict() for c in consultas])

@consulta_bp.route('/<int:consulta_id>', methods=['PUT'])
def update_consulta(consulta_id):
    data = request.get_json()
    data_date = datetime.strptime(data['data'], '%Y-%m-%d').date() if 'data' in data else None
    horario_time = datetime.strptime(data['horario'], '%H:%M').time() if 'horario' in data else None
    consulta = ConsultaRepository.update(consulta_id, data_date, horario_time, data.get('descricao'))
    if consulta:
        return jsonify(consulta.to_dict())
    return jsonify({'error': 'Consulta não encontrada'}), 404

@consulta_bp.route('/<int:consulta_id>', methods=['DELETE'])
def delete_consulta(consulta_id):
    consulta = ConsultaRepository.delete(consulta_id)
    if consulta:
        return jsonify({'message': 'Consulta excluída'})
    return jsonify({'error': 'Consulta não encontrada'}), 404
