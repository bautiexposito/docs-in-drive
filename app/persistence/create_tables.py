# Correr script para crear tablas en la base de datos
# python -m app.persistence.create_tables

from app.persistence.database import Base, engine
from app.model.local_file import LocalFile
from app.model.user import User

Base.metadata.create_all(bind=engine)
