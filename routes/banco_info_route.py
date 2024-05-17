from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.cp_schema
import GestionDePagosBackend.models.cp_model

banco_info = APIRouter(prefix="/banco_info")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@banco_info.get("/listar-banco_info", response_model=List[GestionDePagosBackend.config.schemas.banco_info_schema.BancoInfo])
async def obtener_bancos_info(db:Session=Depends(get_db)):
    bancos_info = db.query(GestionDePagosBackend.models.banco_info_model.BancoInfo).all()
    bancos_info.reverse()
    return bancos_info