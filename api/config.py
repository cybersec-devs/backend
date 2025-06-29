from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Config:
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True

    # Correção no nome da variável (de DATABASE para DATABASE)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///hospital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações adicionais recomendadas
    SECRET_KEY = os.getenv('SECRET_KEY', '$3gur@nc@C1b3rn3rt1c@')
    JSON_SORT_KEYS = False  # Mantém ordem dos campos no JSON