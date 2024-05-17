from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.cp_schema
import GestionDePagosBackend.models.cp_model

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