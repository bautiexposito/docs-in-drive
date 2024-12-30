# FastAPI Drive Inventory Application

Bienvenido a la aplicación FastAPI Drive Inventory, una solución desarrollada en Python utilizando FastAPI para inventariar todos los archivos pertenecientes a la unidad de Google Drive de un usuario y almacenarlos en una Base de Datos.

## Características

- **Autenticación con Google Drive**: Conéctate y autentica tu cuenta de Google Drive.
- **Inventario de Archivos**: Extrae y almacena metadatos de tus archivos en Google Drive.
- **Gestión de Archivos Locales**: Gestiona archivos almacenados localmente en tu base de datos.
- **API RESTful**: Endpoints bien definidos para operaciones CRUD (Create, Read, Update, Delete).

## Requisitos

- Python 3.11 o superior
- Dependencias enumeradas en `requirements.txt`
- Credenciales de Google API (client_secrets.json y credentials_module.json)
- Base de datos SQL instalada

## Documentación

- Postman: https://documenter.getpostman.com/view/24383801/2sAYJ4ifsF
- Google Drive API: https://developers.google.com/drive/api/guides/about-sdk?hl=es-419

## Instalación

1. **Clona el repositorio**:

   ```sh
   git clone https://github.com/bautiexposito/docs-in-drive
   cd docs-in-drive
```

2. **Configurar Variables de Entorno**

Crea un archivo .env en la raíz del proyecto para almacenar las variables de entorno necesarias. 
Ejemplo:
   ```sh
   DATABASE_URL= your_database_url_here
   EMAIL_PASSWORD= your_email_password_here
   GOOGLE_CLIENT_ID= your_client_id_here
   GOOGLE_CLIENT_SECRET= your_secret_key_here
```

3. **Obtener Credenciales de Google API**

   - Ingresar a: https://console.cloud.google.com/
   - Habilitar Google Drive API
   - Configurar pantalla de consentimiento
   - Generar credenciales y guardarlas como 'client_secrets.json', dentro de la carpeta '/app/credentials'
   - En el archivo .env modificar las variables 'GOOGLE_CLIENT_ID' y 'GOOGLE_CLIENT_SECRET' segun los valores generados en su nuevo archivo 'client_secrets.json'

4. **Configurar Correo Electrónico**

   Para poder enviarle un correo al propietario del archivo de drive, cuando la visibilidad de este archivo es modificado.

   - Ingresar al siguiente archivo dentro del repositorio: 'app/service/email.py'
   - Modificar el valor de la variable 'email_sender', colocando su correo @gmail.com
   - Ingresar a: https://myaccount.google.com/u/4/apppasswords
   - Generar una contraseña de aplicacion y guardarla en el archivo .env dentro de la variable 'EMAIL_PASSWORD'

5. **Crear un Entorno Virtual**
   
   En Windows:
   ```sh
   python -m venv venv
   venv\Scripts\activate
```

6. **Instalar Dependencias**

   pip install -r requirements.txt

7. **Configurar el Archivo settings.yaml**

8. **Crear la Base de Datos**

   - Modificar la URL de la variable 'DATABASE_URL' en el archivo .env
   - Ejecutar el script create_tables.py dentro de la carpeta 'persistence'
   - Ejecutar las querys dentro del archivo 'inventario.sql'

9. **Ejecutar la Aplicación**

   uvicorn app.main:app --reload

10. **Ejecutar Tests (Opcional)**

   pytest
