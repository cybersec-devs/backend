from models.paciente import Paciente
from models.medico import Medico
from config import db
from sqlalchemy.exc import IntegrityError,SQLAlchemyError


class PacienteRepository:
    @staticmethod
    def create(nome, medico_id):
        # Valida se o médico existe
        medico = Medico.query.get(medico_id)
        if not medico:
            return {'error': f'Médico com ID {medico_id} não encontrado.'}, 404

        # Cria e salva o paciente
        paciente = Paciente(nome=nome, medico_id=medico_id)
        db.session.add(paciente)
        db.session.commit()

        return paciente.to_dict(), 201

    @staticmethod
    def get_all():
        return Paciente.query.all(), 200  

    @staticmethod
    def get_by_id(paciente_id):
        paciente = Paciente.query.get(paciente_id)
        if not paciente:
            return {'error': f'Paciente com ID {paciente_id} não encontrado.'}, 404
        return paciente.to_dict(), 200        

    @staticmethod
    def get_by_medico(medico_id):
        medico = Medico.query.get(medico_id)
        if not medico:
            return {'error': f'Médico com ID {medico_id} não encontrado.'}, 404
        paciente = Paciente.query.filter_by(medico_id=medico_id).all()
        return paciente.to_dict(), 200  
    
    @staticmethod
    def update(paciente_id, nome=None, medico_id=None):
        paciente = Paciente.query.get(paciente_id)
        medico = Medico.query.get(medico_id)
        if not medico:
            return {'error': f'Médico com ID {medico_id} não encontrado.'}, 404        
        
        if not paciente:
            return {'error': f'Paciente com ID {paciente_id} não encontrado.'}, 404

        if nome:
            paciente.nome = nome
        if medico_id:
            paciente.medico_id = medico_id

        db.session.commit()
        return paciente.to_dict(), 200

    @staticmethod
    def delete(paciente_id):
        paciente = Paciente.query.get(paciente_id)
        if not paciente:
            return {'error': f'Paciente com ID {paciente_id} não encontrado.'}, 404 
        
        try:
            db.session.delete(paciente)
            db.session.commit()
            return {'message': 'Paciente excluído com sucesso.'}, 204
        except SQLAlchemyError:
            db.session.rollback()
            return {'error': 'Erro ao excluir o paciente.'}, 500    
