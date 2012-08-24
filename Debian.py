
from libhttpclient import HttpClient
from apache import ApacheIndexParser

browser = HttpClient

browse to http://cdimage.debian.org/debian-cd/6.0.4/

recursive:
	ApacheIndexParser(webpage)
	walk
	*.torrent ?
		download
		add to torrentflux

