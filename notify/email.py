#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/28 23:03
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from datetime import datetime


class Email:
    def __init__(self, sender, receiver, subject, attach, text, host, port, password):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.attach = attach
        self.text = text
        self.host = host
        self.port = port
        self.pwd = password

    # The emails will be send if be called.
    def send(self):
        message = MIMEMultipart()

        # header
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = Header(self.subject, 'utf-8')

        # content text
        message.attach(MIMEText(self.text))

        # content attach
        try:
            f = open(self.attach, 'rb')
            bys = f.read()
            f.close()

            filename = "data_backup-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            part = MIMEApplication(bys)
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(part)
        except IOError as e:
            # todo
            logging.error(e)
            return

        try:
            # send email
            smtp = smtplib.SMTP(self.host, self.port)
            print(self.sender, self.pwd)
            logging.info(self.sender, self.pwd)
            smtp.login(self.sender, self.pwd)

            smtp.sendmail(self.sender, self.receiver, message.as_string())
            smtp.quit()
            smtp.close()

        except Exception as e:
            logging.error(e)
            return

    # Format the content of email which will be sent.
    def format(self):
        pass
