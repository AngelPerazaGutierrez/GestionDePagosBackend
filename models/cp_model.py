from sqlalchemy import String, Column, Integer, Date, LargeBinary, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from GestionDePagosBackend.config.db import Base, URL_DATABASE, SessionLocal


class Cp(Base):
    __tablename__ = "cp"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    adjuntos = Column(LargeBinary, nullable=True)
    fecha = Column(Date, nullable=False)
    ciudad = Column(nullable=False)
    nit = Column(Integer, nullable=False)
    tercero = Column(nullable=False)
    concepto = Column(String, nullable=False)
    banco = Column(nullable=False)
    tipo_cuenta = Column(nullable=False)
    numero_cuenta = Column(nullable=False)
    valor = Column(Integer, nullable=False)


def guardar_cp(adjunto, fecha, nit, tercero, concepto, banco, tipo_cuenta, valor):
    session = SessionLocal()
    cp = Cp(adjuntos=adjunto, fecha=fecha, nit=nit, tercero=tercero, concepto=concepto, banco=banco, tipo_cuenta=tipo_cuenta, valor=valor)
    session.add(cp)
    session.commit()
    session.close()

guardar_cp("to do.txt", "2024-05-16", 809012157, "Alianza temporales", "Pago nomina 1Q de mayo", "Banco Bogota", "Ahorros", 15560485)
