from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.cp_schema
import GestionDePagosBackend.models.cp_model

usuario = APIRouter(prefix="/usuario")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



# @usuario.get("/listar-usuario", response_model=List[GestionDePagosBackend.config.schemas.usuario_schema.Usuario])
# async def obtener_usuarios(db:Session=Depends(get_db)):
#     usuarios = db.query(GestionDePagosBackend.models.usuario_model.Usuario).all()
#     usuarios.reverse()
#     return usuarios