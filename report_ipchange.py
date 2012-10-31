#!/usr/bin/env python

# read expected external IP address from config file
from ConfigParser import RawConfigParser

parser = RawConfigParser()
parser.read('report_ipchange.conf')

expected_ip = parser.get('expected', 'ip')
print expected_ip


# determine actual external IP address
from wieistmeineip import External_IP

ip = External_IP()
print ip

# compare
if ip != expected_ip:
	print 'ip has changed. informing admins ...'

	# notify admins about the change
	from mailer import MailTransport, Email
	Email(To=parser.get('expected', 'mailto'), Subject='IP-Adresse hat sich unerwartet geaendert', Text='Neue IP-Adresse: '+ip+'\nErwartet war: '+expected_ip).send(MailTransport())
else:
	print 'ok'