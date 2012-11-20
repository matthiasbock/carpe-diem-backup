#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from ping import ping
from mailer import MailTransport, Email

if ping('kanzler-pc'):
	Email(To='cadibe-it@googlegroups.com', Subject='Der Kanzler ist da').send( MailTransport() )


