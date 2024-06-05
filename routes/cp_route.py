from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.cp_schema
import GestionDePagosBackend.models.cp_model

cp = APIRouter(prefix="/cp")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@cp.get("/listar-todo", response_model=List[GestionDePagosBackend.config.schemas.cp_schema.Cp])
async def obtener_cps(db:Session=Depends(get_db)):
    cps = db.query(GestionDePagosBackend.models.cp_model.Cp).all()
    cps.reverse()
    return cps


@cp.get("/cp-principal", response_model=List[GestionDePagosBackend.config.schemas.cp_schema.Cp])
async def obtener_cps(db:Session=Depends(get_db)):
    cps = db.query(GestionDePagosBackend.models.cp_model.Cp).all()
    cps.reverse()
    return cps[:10]


@cp.post("/registrar-cp")
async def agregar_cp(cp: GestionDePagosBackend.config.schemas.cp_schema.CrearCp, db: Session = Depends(get_db)):
    db_cp = GestionDePagosBackend.models.cp_model.Cp(**cp.dict())
    db.add(db_cp)
    db.commit()
    db.refresh(db_cp)
    return db_cp


@cp.put("/editar-cp/{cp_id}", response_model=GestionDePagosBackend.config.schemas.cp_schema.Cp)
async def editar_cp(cp_id: int, cp: GestionDePagosBackend.config.schemas.cp_schema.Cp,
                    db: Session = Depends(get_db)):
        db_cp = db.query(GestionDePagosBackend.models.cp_model.Cp).filter(
            GestionDePagosBackend.models.cp_model.Cp.id == cp_id).first()

        if not db_cp:
            raise HTTPException(status_code=404, detail="Comprobante no encontrado")

        db.query(GestionDePagosBackend.models.cp_model.Cp).filter(GestionDePagosBackend.models.cp_model.Cp.id == cp_id).update({
            "adjuntos": cp.adjuntos,
            "fecha": cp.fecha,
            "ciudad": cp.ciudad,
            "nit": cp.nit,
            "tercero": cp.tercero,
            "concepto": cp.concepto,
            "banco": cp.banco,
            "tipo_cuenta": cp.tipo_cuenta,
            "numero_cuenta": cp.numero_cuenta,
            "valor": cp.valor
        })
        db.commit()

        return cp


@cp.delete("/eliminar-cp/{cp_id}")
async def eliminar_cp(cp_id: int, db: Session = Depends(get_db)):
    db_cp = db.query(GestionDePagosBackend.models.cp_model.Cp).filter(
        GestionDePagosBackend.models.cp_model.Cp.id == cp_id).first()
    if not db_cp:
        raise HTTPException(status_code=404, detail="Comprobante no encontrado")
    db.delete(db_cp)
    db.commit()
    return {"mensaje": "Comprobante eliminado correctamente"}

