#!/usr/bin/env python

from HTMLParser import HTMLParser
import urllib
import sys  
import pprint

reload(sys)  
sys.setdefaultencoding('utf8')

base_url      = 'http://wiprodigital.com/'
parsed_urls   = []
path          = {}
images        = {}
external_urls = {}

# create a subclass and override the handler methods
#
class MyHTMLParser(HTMLParser):

	l_link = []
	l_img  = []

	def handle_starttag(self, tag, attrs, path=None):
		if tag == 'a' :
			attrs   = dict(attrs)
			self.l_link.append(attrs.get("href", ""))
		if tag == 'img' :
			attrs   = dict(attrs)
			if attrs.get("src", "") not in self.l_img:
				self.l_img.append(attrs.get("src", ""))


def get_links(url):
	global images
	global external_urls

	parser = MyHTMLParser()
	parser.l_link = []
	parser.l_img  = []

	response = urllib.urlopen(base_url+url);
	data =     response.read()
	parser.feed(data)
	
	urls          = get_internal_url(parser.l_link)
	internal_urls = urls[0]

	external_urls[url] = urls[1]
	images[url]        = parser.l_img

	return internal_urls

def get_internal_url(url_list) :
	internal_list = []
	external_list = []

	for url in url_list :
		if base_url in url and url not in internal_list and url != base_url:
			internal_list.append(url)
		elif url not in internal_list and url not in ['#','',base_url] and url.startswith('/#') == 0 :
			external_list.append(url)

	return [internal_list,external_list]

def parse(url) :

	for child_url in get_links(url) :
		# exclude parent-child combinations in order to avoid infinite loop
		if [url,child_url] not in parsed_urls :
			parsed_urls.append([url,child_url])
		#if url not in parsed_urls :
			#parsed_urls.append(url)

			if url not in path:
				path[url] = list()
			path[url].append(child_url)
			parse(child_url)


sitemap = {}
root = 'privacy-policy'
parse(root)

for key in path.keys():
	if key not in sitemap:
		sitemap[key] = {}
	sitemap[key]['internal_links'] = path[key]
	sitemap[key]['external_links'] = external_urls[key]
	sitemap[key]['images']         = images[key]

pprint.pprint(sitemap)
