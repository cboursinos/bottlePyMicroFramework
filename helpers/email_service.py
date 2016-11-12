# -*- coding: utf-8 -*-

import smtplib
import settings

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

smtp_server = settings.smtp_server
smtp_user = settings.smtp_user
smtp_password = settings.smtp_password
smtp_port = settings.smtp_port
membershost = settings.membershost


def send_email(data):
    # data['text'] is the actual message
    # me == my email address
    # you == recipient's email address
    me = smtp_user
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = data['title']
    msg['From'] = me
    msg['To'] = ", ".join(data['to'])



    # Create the body of the message (a plain-text and an HTML version).
    text = data['text'].replace("<br>", "\n")
    html = """\
    <!DOCTYPE html>
<html>
<head>
</head>
<body>
{}
</body>
</html>
    """.format(data['to'][0])

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    if 'path_pdf' in data:
        filename = data['path_pdf']
        f = file(filename)
        attachment = MIMEText(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)

    # Send the message via local SMTP server.
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.

    smtpserver = smtplib.SMTP(smtp_server, smtp_port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(smtp_user, smtp_password)
    smtpserver.sendmail(me, data['to'], msg.as_string())
    smtpserver.close()


def prepare_email_template(data):
    if data['template'] == "new_account":
        data['text'] ="".replace()
        data['title'] = "test"
    return data
