from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.ciudad_schema
import GestionDePagosBackend.models.ciudad_model

ciudad = APIRouter(prefix="/ciudad")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@ciudad.get("/listar-ciudad", response_model=List[GestionDePagosBackend.config.schemas.ciudad_schema.Ciudad])
async def obtener_ciudades(db:Session=Depends(get_db)):
    ciudades = db.query(GestionDePagosBackend.models.ciudad_model.Ciudad).all()
    ciudades.reverse()
    return ciudades


@ciudad.put("/editar-ciudad/{ciudad_id}", response_model=GestionDePagosBackend.config.schemas.ciudad_schema.Ciudad)
async def editar_ciudad(ciudad_id: int, ciudad: GestionDePagosBackend.config.schemas.ciudad_schema.Ciudad,
                    db: Session = Depends(get_db)):
        db_ciudad = db.query(GestionDePagosBackend.models.ciudad_model.Ciudad).filter(
            GestionDePagosBackend.models.ciudad_model.Ciudad.id == ciudad_id).first()

        if not db_ciudad:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")

        db.query(GestionDePagosBackend.models.ciudad_model.Ciudad).filter(GestionDePagosBackend.models.ciudad_model.Ciudad.id == ciudad_id).update({
            "pais": ciudad.pais,
            "ciudad": ciudad.ciudad
        })
        db.commit()

        return ciudad


@ciudad.post("/registrar-ciudad")
async def agregar_ciudad(ciudad: GestionDePagosBackend.config.schemas.ciudad_schema.CrearCiudad, db: Session = Depends(get_db)):
    db_ciudad = GestionDePagosBackend.models.ciudad_model.Ciudad(**ciudad.dict())
    db.add(db_ciudad)
    db.commit()
    db.refresh(db_ciudad)
    return db_ciudad


@ciudad.delete("/eliminar-ciudad/{ciudad_id}")
async def eliminar_ciudad(ciudad_id: int, db: Session = Depends(get_db)):
    db_ciudad = db.query(GestionDePagosBackend.models.ciudad_model.Ciudad).filter(
        GestionDePagosBackend.models.ciudad_model.Ciudad.id == ciudad_id).first()
    if not db_ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    db.delete(db_ciudad)
    db.commit()
    return {"mensaje": "Ciudad eliminada correctamente"}