import asyncio
from src.utils.mail import send_email_background

asyncio.run(send_email_background("dimflix.official@gmail.com", "Test email", "Hello, this is a test email!"))