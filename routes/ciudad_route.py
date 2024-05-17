from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.cp_schema
import GestionDePagosBackend.models.cp_model

ciudad = APIRouter(prefix="/ciudad")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@ciudad.get("/listar-ciudad", response_model=List[GestionDePagosBackend.config.schemas.ciudad_schema.Ciudad])
async def obtener_cps(db:Session=Depends(get_db)):
    ciudades = db.query(GestionDePagosBackend.models.ciudad_model.Ciudad).all()
    ciudades.reverse()
    return ciudades