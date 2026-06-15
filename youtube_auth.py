from google_auth_oauthlib.flow import InstalledAppFlow
def authenticate():

    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret_419549666632-kkpmjfj90u9jva3ersf2u8igs10lac7a.apps.googleusercontent.com.json',
        scopes=["https://www.googleapis.com/auth/youtube"])

    creds=flow.run_local_server()
    return creds