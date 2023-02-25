from email.message import EmailMessage
import ssl, smtplib
import streamlit as st

def send_message_to(message: str, recipient_email: str) -> None:

    sender_email_address = "seppitom@gmail.com"
    sender_email_password = st.secrets["EMAIL_API_PW"]

    subject = "Your generated workout"
    body = message

    em = EmailMessage()
    em["From"] = sender_email_address
    em["To"] = recipient_email
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
        smtp.login(sender_email_address, sender_email_password)
        smtp.sendmail(sender_email_address, recipient_email, em.as_string())