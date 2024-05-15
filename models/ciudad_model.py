from sqlalchemy import String, Column, Integer
from GestionDePagosBackend.config.db import Base

class Ciudad(Base):
    __tablename__ = "ciudad"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    pais = Column(String, default="Colombia", nullable=False)
    ciudad = Column(String, nullable=False)