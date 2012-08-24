#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from mailer import MailTransport, Email

Email(From='Kafka <carpediemd27@web.de>', To='matthias.bock@hu-berlin.de', Subject='Test-Mail').send( MailTransport(Account='carpediemd27@web.de') )

