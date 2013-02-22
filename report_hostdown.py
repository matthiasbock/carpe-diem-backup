#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from ping import ping
from mailer import MailTransport, Email

if not ping('thecus'):
	Email(To='cadibe-it@googlegroups.com', Subject='Fehler: Thecus nicht erreichbar').send( MailTransport() )


