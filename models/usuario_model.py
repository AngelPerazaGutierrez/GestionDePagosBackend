import re
from sqlalchemy import Enum, String, Column, Integer, Date, Text
from GestionDePagosBackend.config.db import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    cedula = Column(Integer(11), nullable=False)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String(30), nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    proceso = Column(Enum('Financiero', 'Nomina', 'Gerencia', 'Tesoreria', 'Administrador'), nullable=False)
    imagen = Column(Text)


    def validate_email(self, email):
        # Expresión regular para validar direcciones de correo electrónico
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(email_regex.match(email))
