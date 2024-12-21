import smtplib
from email.mime.text import MIMEText
from config import config

def send_email_notification(subject, body):
    if not config.is_valid():
        print("Missing email configuration.")
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config.EMAIL_USER
    msg['To'] = config.EMAIL_USER

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
            server.sendmail(config.EMAIL_USER, config.EMAIL_USER, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
