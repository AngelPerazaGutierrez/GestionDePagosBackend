from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from GestionDePagosBackend.config.db import SessionLocal
from typing import List
import GestionDePagosBackend.config.schemas.usuario_schema
import GestionDePagosBackend.models.usuario_model

usuario = APIRouter(prefix="/usuario")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@usuario.get("/listar-usuario", response_model=List[GestionDePagosBackend.config.schemas.usuario_schema.Usuario])
async def obtener_usuarios(db:Session=Depends(get_db)):
    usuarios = db.query(GestionDePagosBackend.models.usuario_model.Usuario).all()
    usuarios.reverse()
    return usuarios

#holaasdsaadsadsa
@usuario.put("/editar-usuario/{usuario_cedula}", response_model=GestionDePagosBackend.config.schemas.usuario_schema.Usuario)
async def editar_usuario(usuario_cedula: int, usuario: GestionDePagosBackend.config.schemas.usuario_schema.Usuario,
                    db: Session = Depends(get_db)):
        db_usuario = db.query(GestionDePagosBackend.models.usuario_model.Usuario).filter(
            GestionDePagosBackend.models.usuario_model.Usuario.cedula == usuario_cedula).first()

        if not db_usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        db.query(GestionDePagosBackend.models.usuario_model.Usuario).filter(GestionDePagosBackend.models.usuario_model.Usuario.cedula == usuario_cedula).update({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "password": usuario.password,
            "email": usuario.email,
            "proceso": usuario.proceso
        })
        db.commit()

        return usuario


@usuario.post("/registrar-usuario")
async def agregar_usuario(banco: GestionDePagosBackend.config.schemas.usuario_schema.CrearUsuario, db: Session = Depends(get_db)):
    db_usuario = GestionDePagosBackend.models.usuario_model.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@usuario.delete("/eliminar-usuario/{usuario_id}")
async def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(GestionDePagosBackend.models.usuario_model.Usuario).filter(
        GestionDePagosBackend.models.usuario_model.Usuario.id == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(db_usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}