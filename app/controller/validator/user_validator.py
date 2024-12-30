from enum import Enum
from typing import Optional

class GenderEnum(str, Enum):
    male = "male"
    female = "female"

class UserValidator:
    @staticmethod
    def validate_first_name(first_name: str) -> str:
        if not first_name or len(first_name.strip()) < 2 or len(first_name) > 100:
            raise ValueError('El nombre debe tener entre 2 y 100 caracteres')
        return first_name.strip()

    @staticmethod
    def validate_last_name(last_name: str) -> str:
        if not last_name or len(last_name.strip()) < 2 or len(last_name) > 100:
            raise ValueError('El apellido debe tener entre 2 y 100 caracteres')
        return last_name.strip()

    @staticmethod
    def validate_email(email: str) -> str:
        if not email:
            raise ValueError('El email es requerido')
        if email.count('@') != 1:
            raise ValueError('El email debe contener exactamente un @')
        return email.lower()

    @staticmethod
    def validate_address(address: Optional[str]) -> Optional[str]:
        if address is not None:
            if len(address.strip()) < 5:
                raise ValueError('La direccion debe tener al menos 5 caracteres')
            if len(address) > 500:
                raise ValueError('La direccion no debe exceder los 500 caracteres')
            return address.strip()
        return None

    @staticmethod
    def validate_gender(gender: str) -> str:
        try:
            return GenderEnum(gender).value
        except ValueError:
            raise ValueError('Genero invalido. Debe ser "male" o "female"')

    @classmethod
    def validate(cls, data: dict) -> dict:
        validated_data = {}
        validated_data['first_name'] = cls.validate_first_name(data['first_name'])
        validated_data['last_name'] = cls.validate_last_name(data['last_name'])
        validated_data['email'] = cls.validate_email(data['email'])
        validated_data['gender'] = cls.validate_gender(data['gender'])

        if 'address' in data:
            validated_data['address'] = cls.validate_address(data['address'])
        
        return validated_data
