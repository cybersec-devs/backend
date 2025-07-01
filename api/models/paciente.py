from config import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    medico = db.relationship('Medico', backref=db.backref('pacientes', lazy=True))

    def __init__(self, nome, medico_id):
        self.nome = nome
        self.medico_id = medico_id

    def __repr__(self):
        return f'<Paciente {self.nome}>'


    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'medico_id': self.medico_id,
            'medico': {
                'id': self.medico.id,
                'nome': self.medico.nome,
                'crm': self.medico.crm,
                'especialidade': self.medico.especialidade
            } if self.medico else None
        }

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'nome': self.nome,
    #         'medico_id': self.medico_id
    #     }