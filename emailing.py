import os
import smtplib
import ssl
import imghdr
from email.message import EmailMessage


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New object detected by webcamPythonApp"
    email_message.set_content("Hello, we detected something by your web camera")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    host = "smtp.gmail.com"
    port = 465
    username = "gaidukpetro@gmail.com"
    password = os.getenv("PORTF_PASS_EMAIL")
    receiver = "gaidukpetro@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())


if __name__ == "__main__":
    send_email("images/webcam_app_22.png")