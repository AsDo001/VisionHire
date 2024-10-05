import aiosmtplib
from email.message import EmailMessage
import src.config as cfg

async def send_email_background(email_to: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = "your-email@example.com"
    message["To"] = email_to
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(
        message,
        hostname=cfg.SMTP_HOST,
        port=cfg.SMTP_PORT,
        username=cfg.EMAIL,
        password=cfg.EMAIL_PASSWORD,
        use_tls=False,
    )