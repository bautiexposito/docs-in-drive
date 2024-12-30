from unittest.mock import MagicMock
from app.service.local_file_service import LocalFileService
from app.model.local_file import LocalFile, Visibility

def test_get_all_files():
    db_mock = MagicMock()
    file_mock_1 = LocalFile(
        id=1,
        id_drive="drive_1",
        name="requerimientos1",
        extension="txt",
        emailOwner="bautistaexposito@gmail.com",
        visibility=Visibility.public,
        lastModified="2024-12-01T10:00:00",
    )
    file_mock_2 = LocalFile(
        id=2,
        id_drive="drive_2",
        name="requerimientos2",
        extension="txt",
        emailOwner="juan@perez.com",
        visibility=Visibility.private,
        lastModified="2024-12-02T12:00:00",
    )
    db_mock.query.return_value.all.return_value = [file_mock_1, file_mock_2]

    files = LocalFileService.get_all_files(db_mock)

    assert len(files) == 2
    assert files[0].name == "requerimientos1"
    assert files[1].visibility == Visibility.private


def test_get_file_found():
    db_mock = MagicMock()
    file_mock = LocalFile(
        id=1,
        id_drive="drive_1",
        name="requerimientos1",
        extension="txt",
        emailOwner="bautistaexposito@gmail.com",
        visibility=Visibility.public,
        lastModified="2024-12-01T10:00:00",
    )
    db_mock.query.return_value.filter.return_value.first.return_value = file_mock

    file = LocalFileService.get_file(db_mock, 1)

    assert file.name == "requerimientos1"


def test_get_file_not_found():
    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.first.return_value = None

    try:
        LocalFileService.get_file(db_mock, 99)
    except ValueError as e:
        assert str(e) == "Archivo no encontrado"


def test_create_file():
    db_mock = MagicMock()
    file_data = {
        "id_drive": "drive_1",
        "name": "requerimientos1",
        "extension": "txt",
        "emailOwner": "bautistaexposito@gmail.com",
        "visibility": Visibility.public,
        "lastModified": "2024-12-01T10:00:00",
    }

    LocalFileService.create_file(db_mock, file_data)

    db_mock.add.assert_called_once()
    db_mock.commit.assert_called_once()


def test_update_file_found():
    db_mock = MagicMock()
    file_mock = LocalFile(
        id=1,
        id_drive="drive_1",
        name="requerimientos1",
        extension="txt",
        emailOwner="bautistaexposito@gmail.com",
        visibility=Visibility.public,
        lastModified="2024-12-01T10:00:00",
    )
    db_mock.query.return_value.filter.return_value.first.return_value = file_mock

    updated_data = {"name": "updated_requerimientos1"}
    file = LocalFileService.update_file(db_mock, 1, updated_data)

    assert file.name == "updated_requerimientos1"


def test_update_file_not_found():
    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.first.return_value = None

    try:
        LocalFileService.update_file(db_mock, 99, {"name": "nonexiste.txt"})
    except ValueError as e:
        assert str(e) == "Archivo no encontrado"


def test_delete_file_found():
    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.delete.return_value = True

    LocalFileService.delete_file(db_mock, 1)

    db_mock.commit.assert_called_once()


def test_delete_file_not_found():
    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.delete.return_value = False

    try:
        LocalFileService.delete_file(db_mock, 99)
    except ValueError as e:
        assert str(e) == "Archivo no encontrado"
