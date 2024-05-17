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