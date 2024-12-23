from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Autenticacion con Google Drive
gauth = GoogleAuth()

# Ruta donde se guardaran las credenciales
gauth.settings_file = "settings.yaml"
gauth.LoadClientConfigFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/client_secrets.json")

# Intentar cargar credenciales guardadas
try:
    gauth.LoadCredentialsFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/credentials_module.json")
    if gauth.credentials is None or gauth.access_token_expired:
        # Si no existen o estan expiradas, reautenticar
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/credentials_module.json")
    else:
        print("Autenticacion cargada desde archivo")
except Exception as e:
    # Si no existe el archivo o hay un error, forzar autenticacion
    print("Autenticacion fallida o no encontrada, solicitando nueva...")
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/credentials_module.json")

# Inicializar Google Drive
drive = GoogleDrive(gauth)
