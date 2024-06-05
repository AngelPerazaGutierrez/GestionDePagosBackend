from sqlalchemy import String, Column, Integer, Date, Enum
from GestionDePagosBackend.models.base import Base
from GestionDePagosBackend.enum.procesos_enum import Procesos


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, index=True, nullable=False, autoincrement=True, primary_key=True)
    cedula = Column(Integer, nullable=False, unique=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    proceso = Column(Enum(Procesos), nullable=False)

