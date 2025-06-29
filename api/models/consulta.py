from config import db
from datetime import date, time

class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    paciente = db.relationship('Paciente', backref=db.backref('consultas', lazy=True))

    def __init__(self, data, horario, descricao, paciente_id):
        self.data = data
        self.horario = horario
        self.descricao = descricao
        self.paciente_id = paciente_id

    def __repr__(self):
        return f'<Consulta {self.id}>'


    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.isoformat(),
            'horario': self.horario.strftime('%H:%M'),
            'descricao': self.descricao,
            'paciente_id': self.paciente_id,
            'paciente': {
                'id': self.paciente.id,
                'nome': self.paciente.nome
            } if self.paciente else None
        }
