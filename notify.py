#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from ping import ping
from mailer import MailTransport, Email

if ping('kanzler-pc'):
	Email(From='Kafka <carpediemd27@web.de>', To='matthias.bock@hu-berlin.de', Subject='Der Kanzler ist da').send( MailTransport(Account='carpediemd27@web.de') )

