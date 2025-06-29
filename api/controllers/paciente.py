from flask import Blueprint, request, jsonify
from repositories.paciente import PacienteRepository

paciente_bp = Blueprint('paciente', __name__,url_prefix='/pacientes')

@paciente_bp.route('', methods=['POST'])
def create_paciente():
    data = request.get_json()
    paciente = PacienteRepository.create(data['nome'], data['medico_id'])
    return jsonify(paciente.to_dict()), 201

@paciente_bp.route('', methods=['GET'])
def get_pacientes():
    response, status = PacienteRepository.get_all()
    # CONVERTER cada paciente em dicionário
    pacientes_dict = [paciente.to_dict() for paciente in response]
    return jsonify(pacientes_dict), status

@paciente_bp.route('/<int:paciente_id>', methods=['GET'])
def get_paciente(paciente_id):
    paciente, status = PacienteRepository.get_by_id(paciente_id)
    if paciente:
        return jsonify(paciente), status
    return jsonify({'error': 'Paciente não encontrado'}), 404

@paciente_bp.route('/medicos/<int:medico_id>/pacientes', methods=['GET'])
def get_pacientes_by_medico(medico_id):
    pacientes = PacienteRepository.get_by_medico(medico_id)
    return jsonify([p.to_dict() for p in pacientes])

@paciente_bp.route('/<int:paciente_id>', methods=['PUT'])
def update_paciente(paciente_id):
    data = request.get_json()
    paciente = PacienteRepository.update(paciente_id, data.get('nome'), data.get('medico_id'))
    if paciente:
        return jsonify(paciente.to_dict())
    return jsonify({'error': 'Paciente não encontrado'}), 404

@paciente_bp.route('/<int:paciente_id>', methods=['DELETE'])
def delete_paciente(paciente_id):
    paciente = PacienteRepository.delete(paciente_id)
    if paciente:
        return jsonify({'message': 'Paciente excluído'})
    return jsonify({'error': 'Paciente não encontrado'}), 404
