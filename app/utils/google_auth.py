from pydrive2.auth import GoogleAuth
import os

current_dir = os.path.dirname(__file__)
settings_path = os.path.abspath(os.path.join(current_dir, '../config/settings.yaml'))

gauth = GoogleAuth()
#gauth.settings['client_config_file'] = 'credentials/client_secret.json'
gauth.settings_file = settings_path
gauth.LocalWebserverAuth()