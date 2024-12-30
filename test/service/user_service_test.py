import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app.service.user_service import UserService
from app.model.user import User, Gender

@pytest.fixture
def db_mock():
    return MagicMock(spec=Session)

@pytest.fixture
def sample_user_data():
    return {
        "first_name": "Juan",
        "last_name": "Perez",
        "email": "juan@perez.com",
        "address": "Sarmiento 300",
        "gender": Gender.male,
    }

def test_get_all_users(db_mock):
    db_mock.query.return_value.all.return_value = [User(id=1, first_name="Juan", last_name="Perez")]
    users = UserService.get_all_users(db_mock)

    assert len(users) == 1
    assert users[0].first_name == "Juan"
    db_mock.query.assert_called_once()

def test_get_user_found(db_mock):
    user_mock = User(id=1, first_name="Juan", last_name="Perez")
    db_mock.query.return_value.filter.return_value.first.return_value = user_mock

    user = UserService.get_user(db_mock, 1)

    assert user.id == 1
    assert user.first_name == "Juan"
    db_mock.query.return_value.filter.return_value.first.assert_called_once()

def test_get_user_not_found(db_mock):
    db_mock.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(ValueError, match="Usuario no encontrado"):
        UserService.get_user(db_mock, 999)

def test_create_user(db_mock, sample_user_data):
    created_user = UserService.create_user(db_mock, sample_user_data)

    assert created_user.first_name == "Juan"
    assert created_user.email == "juan@perez.com"
    db_mock.add.assert_called_once()
    db_mock.commit.assert_called_once()

def test_update_user_found(db_mock, sample_user_data):
    user_mock = User(id=1, **sample_user_data)
    db_mock.query.return_value.filter.return_value.first.return_value = user_mock

    updated_data = {"first_name": "Carlos"}
    updated_user = UserService.update_user(db_mock, 1, updated_data)

    assert updated_user.first_name == "Carlos"
    db_mock.commit.assert_called_once()

def test_update_user_not_found(db_mock):
    db_mock.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(ValueError, match="Usuario no encontrado"):
        UserService.update_user(db_mock, 999, {"first_name": "Carlos"})

def test_delete_user_found(db_mock):
    user_mock = User(id=1, first_name="Juan", last_name="Perez")
    db_mock.query.return_value.filter.return_value.first.return_value = user_mock

    result = UserService.delete_user(db_mock, 1)

    assert result is True
    db_mock.delete.assert_called_once_with(user_mock)
    db_mock.commit.assert_called_once()

def test_delete_user_not_found(db_mock):
    db_mock.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(ValueError, match="Usuario no encontrado"):
        UserService.delete_user(db_mock, 999)
