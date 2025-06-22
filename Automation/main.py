from gmail_service import get_gmail_service
from send_utils import send_email

if __name__ == '__main__':
    service = get_gmail_service()
    send_email(
        service=service,
        sender="achyutareddy224@gmail.com",
        to="ksreenivasulu809@gmail.com",
        subject="Test Email from Python",
        body="Hello from Gmail API and Python!"
    )