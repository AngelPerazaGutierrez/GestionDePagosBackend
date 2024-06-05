from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from GestionDePagosBackend.models.base import Base

URL_DATABASE = "mysql+pymysql://root:@localhost:3306/database_cp"

engine = create_engine(URL_DATABASE)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



