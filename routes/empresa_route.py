from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.empresa_schema
import GestionDePagosBackend.models.empresa_model

empresa = APIRouter(prefix="/empresa")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@empresa.get("/listar-empresa", response_model=List[GestionDePagosBackend.config.schemas.empresa_schema.Empresa])
async def obtener_empresas(db:Session=Depends(get_db)):
    empresas = db.query(GestionDePagosBackend.models.empresa_model.Empresa).all()
    empresas.reverse()
    return empresas


@empresa.put("/editar-empresa/{empresa_nit}", response_model=GestionDePagosBackend.config.schemas.empresa_schema.Empresa)
async def editar_empresa(empresa_nit: int, empresa: GestionDePagosBackend.config.schemas.empresa_schema.Empresa,
                    db: Session = Depends(get_db)):
        db_empresa = db.query(GestionDePagosBackend.models.empresa_model.Empresa).filter(
            GestionDePagosBackend.models.empresa_model.Empresa.nit == empresa_nit).first()

        if not db_empresa:
            raise HTTPException(status_code=404, detail="Empresa no encontrada")

        db.query(GestionDePagosBackend.models.empresa_model.Empresa).filter(GestionDePagosBackend.models.empresa_model.Empresa.nit == empresa_nit).update({
            "nombre_empresa": empresa.nombre_empresa,
            "tipo_cuenta1": empresa.tipo_cuenta1,
            "nombre_banco1": empresa.nombre_banco1,
            "numero_cuenta1": empresa.numero_cuenta1,
            "ciudad": empresa.ciudad
        })
        db.commit()

        return empresa


@empresa.post("/registrar-empresa")
async def agregar_empresa(empresa: GestionDePagosBackend.config.schemas.empresa_schema.CrearEmpresa, db: Session = Depends(get_db)):
    db_empresa = GestionDePagosBackend.models.empresa_model.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@empresa.delete("/eliminar-empresa/{empresa_id}")
async def eliminar_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(GestionDePagosBackend.models.empresa_model.Empresa).filter(
        GestionDePagosBackend.models.empresa_model.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    db.delete(db_empresa)
    db.commit()
    return {"mensaje": "Empresa eliminada correctamente"}