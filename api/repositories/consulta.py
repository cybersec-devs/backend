from models.consulta import Consulta
from models.paciente import Paciente
from config import db
from datetime import datetime, date
from sqlalchemy.exc import SQLAlchemyError

class ConsultaRepository:
    @staticmethod
    def create(data, horario, descricao, paciente_id):
        print(horario)
        # Valida se o paciente existe
        paciente = Paciente.query.get(paciente_id)
        if not paciente:
            return {'error': f'Paciente com ID {paciente_id} não encontrado.'}, 404
 
        # Cria e salva a consulta    
        # Conversão correta
        #data_obj = datetime.strptime(data, '%d/%m/%Y').date()
        # Verifica se `data` é uma string, se for, converte
        if isinstance(data, str):
            data_obj = datetime.strptime(data, '%d/%m/%Y').date()
        elif isinstance(data, date):
            data_obj = data
        else:
            data_obj = date.today()

        #horario_obj = datetime.strptime(horario, '%H:%M:%S').time()
        from datetime import time

        if isinstance(horario, str):
            horario_obj = datetime.strptime(horario, '%H:%M:%S').time()
        elif isinstance(horario, time):
            horario_obj = horario
        else:
            horario_obj = datetime.now().time()  # <-- horário atual

        
        consulta = Consulta(data=data_obj, horario=horario_obj, descricao=descricao, paciente_id=paciente_id)
        db.session.add(consulta)
        db.session.commit()
        return consulta.to_dict(), 201

    @staticmethod
    def get_all():
        consultas = Consulta.query.all()
        return [c.to_dict() for c in consultas], 200

    @staticmethod
    def get_by_id(consulta_id):
        consulta = Consulta.query.get(consulta_id)
        if consulta:
            return consulta.to_dict(), 200
        return {'error': f'Consulta com ID {consulta_id} não encontrada.'}, 404

    @staticmethod
    def get_by_paciente(paciente_id):
        paciente = Paciente.query.get(paciente_id)
        if not paciente:
            return {'error': f'Paciente com ID {paciente_id} não encontrado.'}, 404
        consultas_pacientes = Consulta.query.filter_by(paciente_id=paciente_id).all()
        return consultas_pacientes.to_dict(), 200          

    @staticmethod
    def update(consulta_id, data, horario, descricao=None):
        consulta = Consulta.query.get(consulta_id)

        if consulta:            
            if data:
                # Converte string para objeto datetime.date
                data_obj =  datetime.strptime(data, '%d/%m/%Y').date()
                consulta.data = data_obj
            if horario:
                horario_obj = datetime.strptime(horario, '%H:%M:%S').time()
                consulta.horario = horario_obj
            if descricao is not None:
                consulta.descricao = descricao
            db.session.commit()
        return consulta.to_dict(), 200

    @staticmethod
    def delete(consulta_id):    
        consulta = Consulta.query.get(consulta_id)
        if not consulta:
            return {'error': f'A consulta com ID {consulta_id} não encontrado.'}, 404 
        
        try:
            db.session.delete(consulta)
            db.session.commit()
            return {'message': 'Consulta excluída com sucesso.'}, 200
        except SQLAlchemyError:
            db.session.rollback()
            return {'error': 'Erro ao excluir o paciente.'}, 500    


