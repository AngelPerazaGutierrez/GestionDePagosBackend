from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from GestionDePagosBackend.config.db import Base

class Banco(Base):
    __tablename__ = "banco"
    id = Column(Integer, index=True, nullable=False, autoincrement=True)
    tipo_cuenta = Column(String, nullable=False)
    nit = Column(Integer, primary_key=True, index=True, nullable=False)
    # Relación con la tabla de información de los bancos
    banco_info_nit = Column(Integer, ForeignKey('banco_info.nit'))
    banco_info = relationship("BancoInfo", back_populates="bancos")





