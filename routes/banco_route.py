from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.cp_schema
import GestionDePagosBackend.models.cp_model

banco = APIRouter(prefix="/banco")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@banco.get("/listar-banco", response_model=List[GestionDePagosBackend.config.schemas.banco_schema.Banco])
async def obtener_bancos(db:Session=Depends(get_db)):
    bancos = db.query(GestionDePagosBackend.models.banco_model.Banco).all()
    bancos.reverse()
    return bancos