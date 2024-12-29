from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.persistence.database import Base
from datetime import datetime, timezone
from enum import Enum as PyEnum

class Visibility(PyEnum):
    public = "public"
    private = "private"

class LocalFile(Base):
    __tablename__ = "local_files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_drive = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    extension = Column(String(255), nullable=False)
    emailOwner = Column(String(255), nullable=False)
    visibility = Column(Enum(Visibility), nullable=False)
    lastModified = Column(DateTime, nullable=False)
