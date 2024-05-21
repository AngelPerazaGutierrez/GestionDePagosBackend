from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.banco_schema
import GestionDePagosBackend.models.banco_model

banco = APIRouter(prefix="/banco")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@banco.get("/listar-todo", response_model=List[GestionDePagosBackend.config.schemas.banco_schema.Banco])
async def obtener_bancos(db:Session=Depends(get_db)):
    bancos = db.query(GestionDePagosBackend.models.banco_model.Banco).all()
    bancos.reverse()
    return bancos


@banco.put("/editar-banco/{banco_id}", response_model=GestionDePagosBackend.config.schemas.banco_schema.Banco)
async def editar_cp(banco_id: int, banco: GestionDePagosBackend.config.schemas.banco_schema.Banco,
                    db: Session = Depends(get_db)):
        db_banco = db.query(GestionDePagosBackend.models.banco_model.Banco).filter(
            GestionDePagosBackend.models.banco_model.Banco.id == banco_id).first()

        if not db_banco:
            raise HTTPException(status_code=404, detail="Banco no encontrado")

        db.query(GestionDePagosBackend.models.banco_model.Banco).filter(GestionDePagosBackend.models.banco_model.Banco.id == banco_id).update({
            "nit": banco.nit,
            "tipo_cuenta": banco.tipo_cuenta,
            "nombre_banco": banco.nombre_banco
        })
        db.commit()

        return banco


@banco.post("/registrar-banco")
async def agregar_banco(banco: GestionDePagosBackend.config.schemas.banco_schema.CrearBanco, db: Session = Depends(get_db)):
    db_banco = GestionDePagosBackend.models.banco_model.Banco(**banco.dict())
    db.add(db_banco)
    db.commit()
    db.refresh(db_banco)
    return db_banco


@banco.delete("/eliminar-banco/{banco_id}")
async def eliminar_banco(banco_id: int, db: Session = Depends(get_db)):
    db_banco = db.query(GestionDePagosBackend.models.banco_model.Banco).filter(
        GestionDePagosBackend.models.banco_model.Banco.id == banco_id).first()
    if not db_banco:
        raise HTTPException(status_code=404, detail="Banco no encontrado")
    db.delete(db_banco)
    db.commit()
    return {"mensaje": "Banco eliminado correctamente"}

