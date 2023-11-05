from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

def load_credentials():
    load_dotenv()
    email_login = os.getenv("EMAIL_LOGIN")
    email_pass = os.getenv("EMAIL_PASSWORD")
    return email_login, email_pass

def get_file_content(file_name):
    try:
        full_file_name = file_name + '.txt'
        with open(full_file_name, 'r') as file:
            file_text = file.read()
            return file_text
    except FileNotFoundError:
        return None

def send_email(email_login, email_pass, email_title, email_recipient, file_content):
    try:
        if file_content is not None:
            msg = EmailMessage()
            msg['From'] = email_login
            msg['To'] = email_recipient
            msg['Subject'] = email_title
            msg.set_content(file_content)

            smtp_server = 'poczta.interia.pl'
            port = 465

            with smtplib.SMTP_SSL(smtp_server, port) as server:
                server.ehlo()
                server.login(email_login, email_pass)
                server.send_message(msg)
            return 'Email was sent.'
        else:
            return 'File was not found or cannot be open'
    except Exception as e:
        return f'Error: {str(e)}'

def main():
    email_login, email_pass = load_credentials()
    email_title = 'Test mail'
    email_recipient = 'debugtestmail@interia.pl'
    file_name = input('Enter file name: ')
    file_content = get_file_content(file_name)
    send_email(email_login, email_pass, email_title, email_recipient, file_content)

if __name__ == '__main__':
    main()

