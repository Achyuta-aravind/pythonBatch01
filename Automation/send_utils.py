import base64
from email.message import EmailMessage

def send_email(service, sender, to, subject, body):
    """
    Sends an email via the Gmail API
    """
    message = EmailMessage()
    message.set_content(body)
    message['To'] = to
    message['From'] = sender
    message['Subject'] = subject

    # Encode message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send via Gmail API
    create_message = {'raw': encoded_message}
    sent = service.users().messages().send(userId="me", body=create_message).execute()
    print(f"✅ Email sent! Message ID: {sent['id']}")
    return sent
