#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from ConfigParser import RawConfigParser
from wieistmeineip import External_IP

from email.mime.text import MIMEText
from smtplib import SMTP

class MailTransport:
	def __init__(self, Account='default'):
		parser = RawConfigParser()
		parser.read('mailer.conf')
		self.Host = parser.get(Account, 'Host')
		self.Port = parser.get(Account, 'Port')
		self.User = parser.get(Account, 'User')
		self.Password = parser.get(Account, 'Password')
		self.From = parser.get(Account, 'From')
		self.LocalIP = External_IP()

class Email:
	def __init__(self, To='', Subject='', Text=''):
		self.To = To
		self.Subject = Subject
		self.Text = Text

	def send(self, Transport=None):
		if Transport is None:
			print "Error: Account not defined!"
			return

		msg = MIMEText( self.Text )
		msg['Subject'] = self.Subject
		msg['From'] = Transport.From
		msg['To'] = self.To

		connection = SMTP( Transport.Host, Transport.Port, Transport.LocalIP )
		connection.set_debuglevel( 1 )
		connection.ehlo( Transport.LocalIP )
		connection.starttls()
		connection.ehlo( Transport.LocalIP )
		connection.login( Transport.User, Transport.Password )
		connection.sendmail( Transport.From, [self.To], msg.as_string() )
		connection.quit()

