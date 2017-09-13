import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# path variables
datafile = os.path.join(os.path.dirname(__file__), 'data.csv')
template = os.path.join(os.path.dirname(__file__), 'template.html')

# variables used for connecting and sending messages via smtp
host = 'smtp.gmail.com'
port = 587
username = '<your email here>'
password = '<your password here>'
from_email = username

def read_data():
    data_list = []
    with open(datafile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(row)
    return data_list

def update_data(data_list):
    fieldnames = ['birthday', 'name', 'email', 'tosend']
    with open(datafile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)

def make_send_message(person):
    html_msg = open(template, 'r').read().format(name=person.get('name'))
    mime_msg = MIMEMultipart("alternative")
    text_msg = 'Happy Birthday!!'
    mime_msg["From"] = from_email
    mime_msg["To"] = person.get('email')
    mime_msg["Subject"] = "A very happy birthday to you!"
    plain = MIMEText(text_msg, 'plain')
    html = MIMEText(html_msg, 'html')
    mime_msg.attach(plain)
    mime_msg.attach(html)
    try:
        email_conn = smtplib.SMTP(host, port)
        email_conn.starttls()
        email_conn.login(username, password)
        email_conn.sendmail(from_email, [person['email']], mime_msg.as_string())
        email_conn.quit()
        return True
    except:
        return False





