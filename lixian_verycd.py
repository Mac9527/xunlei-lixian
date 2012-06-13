
import urllib2
import re

def parse_links(html):
	html = re.search(r'<!--eMule begin-->.*?<!--eMule end-->', html, re.S).group()
	links = re.findall(r'value="([^"]+)"', html)
	return [x for x in links if x.startswith('ed2k://')]

def verycd_links(url):
	assert url.startswith('http://www.verycd.com/topics/')
	return parse_links(urllib2.urlopen(url).read())

extend_link = verycd_links
