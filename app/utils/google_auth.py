from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

class GoogleDriveAuth:
    def __init__(self):
        self.gauth = GoogleAuth() # Autenticacion con Google Drive
        self.drive = None
        self.gauth.settings_file = "settings.yaml"

    def authenticate(self):
        # Configuracion y autenticacion
        self.gauth.LoadClientConfigFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/client_secrets.json")
        try:
            self.gauth.LoadCredentialsFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/credentials_module.json")
            if self.gauth.credentials is None or self.gauth.access_token_expired:
                # Si no existen o estan expiradas, reautenticar
                self.gauth.LocalWebserverAuth()
                self.gauth.SaveCredentialsFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/credentials_module.json")
            else:
                print("Autenticacion cargada desde archivo")
        except Exception as e:
            # Si no existe el archivo o hay un error, forzar autenticacion
            print("Autenticacion fallida o no encontrada, solicitando nueva...")
            self.gauth.LocalWebserverAuth()
            self.gauth.SaveCredentialsFile("C:/Users/Marcelo/Documents/justSomeCodes!/Inventario/credentials/credentials_module.json")
        # Inicializar Google Drive
        self.drive = GoogleDrive(self.gauth)
        return self.drive
