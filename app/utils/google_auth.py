import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

class GoogleDriveAuth:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.drive = None
        
        project_base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.gauth.settings_file = os.path.join(project_base_path, "app", "utils", "settings.yaml")

    def authenticate(self):
        project_base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        client_secrets_path = os.path.join(project_base_path, "credentials", "client_secrets.json")
        credentials_path = os.path.join(project_base_path, "credentials", "credentials_module.json")

        # Configuracion y autenticacion
        self.gauth.LoadClientConfigFile(client_secrets_path)
        try:
            self.gauth.LoadCredentialsFile(credentials_path)
            if self.gauth.credentials is None or self.gauth.access_token_expired:
                # Si no existen o estan expiradas, reautenticar
                self.gauth.LocalWebserverAuth()
                self.gauth.SaveCredentialsFile(credentials_path)
            else:
                print("Autenticacion cargada desde archivo")
        except Exception as e:
            # Si no existe el archivo o hay un error, forzar autenticacion
            print("Autenticacion fallida o no encontrada, solicitando nueva...")
            self.gauth.LocalWebserverAuth()
            self.gauth.SaveCredentialsFile(credentials_path)

        self.drive = GoogleDrive(self.gauth)
        return self.drive
