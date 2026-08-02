from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv
import os
load_dotenv()
def authenticate():
    #print("GOOGLE ID-",os.getenv('GOOGLE_CLIENT_SECRET_FILE'))
    flow = InstalledAppFlow.from_client_secrets_file(
        os.getenv('GOOGLE_CLIENT_SECRET_FILE'),
        scopes=["https://www.googleapis.com/auth/youtube"])

    creds=flow.run_local_server()
    return creds