USE inventario;

-- nueva tabla para registrar los cambios de visibilidad
CREATE TABLE visibility_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_id VARCHAR(255) NOT NULL,
    visibility VARCHAR(50) NOT NULL,
    changed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES local_files(id_drive)
);

/*
este trigger registra automaticamente los cambios en la tabla visibility_history
cuando se acutalice la visibilidad en local_files
*/
DELIMITER $$
CREATE TRIGGER before_visibility_update
BEFORE UPDATE ON local_files
FOR EACH ROW
BEGIN
    IF NEW.visibility != OLD.visibility THEN
        INSERT INTO visibility_history (file_id, visibility, changed_at)
        VALUES (OLD.id_drive, OLD.visibility, NOW());
    END IF;
END$$
DELIMITER ;

-- vista para consultar todos los archivos que alguna vez fueron publicos
CREATE VIEW public_files_history AS
SELECT DISTINCT 
    lf.id_drive AS file_id,
    lf.name,
    lf.extension,
    lf.emailOwner,
    vh.visibility,
    vh.changed_at
FROM local_files lf
JOIN visibility_history vh ON lf.id_drive = vh.file_id
WHERE vh.visibility = 'public';

INSERT INTO visibility_history (file_id, visibility, changed_at)
SELECT id_drive, visibility, NOW()
FROM local_files;
