import os
import firebase_admin

from firebase_admin import credentials
from firebase_admin import messaging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

cred_path = os.path.join(
    BASE_DIR,
    "notifications",
    "firebase-key.json"
)

cred = credentials.Certificate(cred_path)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


def send_push(title, body, device_token):

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=device_token
    )

    response = messaging.send(message)

    print("✅ PUSH SENT:", response)