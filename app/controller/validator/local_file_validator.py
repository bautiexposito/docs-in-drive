from fastapi import HTTPException
from enum import Enum
from datetime import datetime

class Visibility(str, Enum):
    public = "public"
    private = "private"

class LocalFileValidator:
    @staticmethod
    def validate_id_drive(id_drive: str) -> str:
        if not id_drive or len(id_drive.strip()) == 0:
            raise HTTPException(status_code=400, detail='El ID de Drive es requerido')
        return id_drive.strip()

    @staticmethod
    def validate_name(name: str) -> str:
        if not name or len(name.strip()) == 0 or len(name.strip()) > 255:
            raise HTTPException(status_code=400, detail='El nombre del archivo es requerido y no puede superar los 255 caracteres')
        return name.strip()

    @staticmethod
    def validate_extension(extension: str) -> str:
        if not extension or len(extension.strip()) == 0:
            raise HTTPException(status_code=400, detail='La extensión del archivo es requerida')
        return extension.strip()

    @staticmethod
    def validate_email_owner(emailOwner: str) -> str:
        if not emailOwner:
            raise HTTPException(status_code=400, detail='El email del propietario es requerido')
        if emailOwner.count('@') != 1:
            raise HTTPException(status_code=400, detail='El email debe contener exactamente un @')
        return emailOwner.lower()

    @staticmethod
    def validate_visibility(visibility: str) -> str:
        try:
            return Visibility(visibility).value
        except ValueError:
            raise HTTPException(status_code=400, detail='Visibilidad invalida. Debe ser "public" o "private"')

    @staticmethod
    def validate_last_modified(lastModified: datetime) -> datetime:
        if not isinstance(lastModified, datetime):
            raise HTTPException(status_code=400, detail='La fecha de ultima modificacion debe ser un datetime valido')
        return lastModified

    @classmethod
    def validate(cls, data: dict) -> dict:
        validated_data = {}
        validated_data['id_drive'] = cls.validate_id_drive(data['id_drive'])
        validated_data['name'] = cls.validate_name(data['name'])
        validated_data['extension'] = cls.validate_extension(data['extension'])
        validated_data['emailOwner'] = cls.validate_email_owner(data['emailOwner'])
        validated_data['visibility'] = cls.validate_visibility(data['visibility'])
        validated_data['lastModified'] = cls.validate_last_modified(data['lastModified'])
        return validated_data
