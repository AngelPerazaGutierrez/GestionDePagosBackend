from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from GestionDePagosBackend.config.db import Base

class BancoInfo(Base):
    __tablename__ = "banco_info"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nit = Column(Integer, ForeignKey('banco.nit'), nullable=False)
    nombre = Column(String, nullable=False)
    # Relación con la tabla de bancos
    banco = relationship("Banco", back_populates="banco_info")
