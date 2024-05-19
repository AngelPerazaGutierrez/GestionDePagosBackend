import re
from sqlalchemy import Enum, String, Column, Integer, Date, Text
from GestionDePagosBackend.config.db import Base
from GestionDePagosBackend.enum.procesos_enum import Procesos


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, index=True, nullable=False, autoincrement=True)
    cedula = Column(Integer(11), primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String(30), nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    proceso = Column(Enum(Procesos), nullable=False)

