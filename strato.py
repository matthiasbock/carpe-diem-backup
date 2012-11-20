#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from httpclient import HttpClient

class Strato:
	def __init__(self):
		self.r = HttpClient(debug=True)

	def login(self, username, password):
		self.r.GET('https://www.strato.de/apps/CustomerService')
		f = self.r.Page.findForm(action='https://www.strato.de/apps/CustomerService')
		f.input['identifier'].value = username
		f.input['passwd'].value = password
		self.r.submit(f)
		if "versuchen Sie es erneut." in str(self.r.Page):
			return False
		self.sessionID = self.r.Cookie['SK_Session']
		return True

	def getDomains(self):
		self.r.GET('https://www.strato.de/apps/CustomerService?sessionID='+self.sessionID+'&cID=1&node=kds_DomainManagement&source=menu')
		domains = {}
		key = '<strong class="trimDomain">'
		subkey = '<span class="trimSubdomain">'
		p = self.r.Page.find(key)
		while p > -1:
			p += len(key)
			q = self.r.Page.find('</', p)
			domain = str(self.r.Page)[p:q]
			domains[domain] = []
			p_next = self.r.Page.find(key, q)
			if p_next < 0:
				p_next = len(str(self.r.Page))
			x = self.r.Page.find(subkey, p)
			while x > -1 and x < p_next:
				x += len(subkey)
				y = self.r.Page.find('</', x)
				subdomain = str(self.r.Page)[x:y]
				domains[domain].append(subdomain)
				x = self.r.Page.find(subkey, y)
			p = self.r.Page.find(key, q)
		return domains

if __name__ == '__main__':
	from ConfigParser import RawConfigParser

	parser = RawConfigParser()
	parser.read('strato.conf')
	username = parser.get('Login', 'Username')
	password = parser.get('Login', 'Password')

	s = Strato()
	if s.login(username, password):
		print s.getDomains()

