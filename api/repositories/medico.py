from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from models.medico import Medico
from config import db

# Função para criar um novo Médico
def create_medico(nome, especialidade, crm):
    try:
        medico = Medico(nome=nome, especialidade=especialidade, crm=crm)
        db.session.add(medico)
        db.session.commit()
        return medico.to_dict(), 201  
    except IntegrityError:
        db.session.rollback()
        return {'error': 'CRM já cadastrado. Insira um CRM único.'}, 409

# Função para obter todos os Médicos
def get_medicos():
    medicos = Medico.query.all()
    return [m.to_dict() for m in medicos], 200
    return medicos, 200


# Função para obter um Médico por ID
def get_medico_by_id(medico_id):
    medico = Medico.query.get(medico_id)
    if not medico:
        return {'error': f'Médico com ID {medico_id} não encontrado.'}, 404
    return medico.to_dict(), 200


# Função para atualizar um Médico
def update_medico(medico_id, nome=None, especialidade=None, crm=None):
    medico = Medico.query.get(medico_id)
    # Verifica se o médico existe
    if not medico:
        return {'error': f'Médico com ID {medico_id} não encontrado.'}, 404
    
    try:
        if nome:
            medico.nome = nome
        if especialidade:
            medico.especialidade = especialidade
        if crm:
            medico.crm = crm        
        db.session.commit()
        return medico.to_dict(), 201  
    except IntegrityError:
        db.session.rollback()
        return {'error': 'CRM já cadastrado. Insira um CRM único.'}, 409
    

# Função para excluir um Médico

def delete_medico(medico_id):
    medico = Medico.query.get(medico_id)
    if not medico:
        return {'error': f'Médico com ID {medico_id} não encontrado.'}, 404

    try:
        db.session.delete(medico)
        db.session.commit()
        return {'message': 'Médico excluído com sucesso.'}, 200
    except SQLAlchemyError:
        db.session.rollback()
        return {'error': 'Erro ao excluir o médico.'}, 500
