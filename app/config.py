import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    GMAIL_CREDENTIALS_FILE = "credentials.json"
    GMAIL_TOKEN_FILE = "token.json"
