#!/usr/bin/env python

from HTMLParser import HTMLParser
import urllib
import sys  
import pprint

# set encoding
reload(sys)  
sys.setdefaultencoding('utf8')

# initialise gloabal variables
base_url      = 'http://wiprodigital.com/'
parsed_urls   = []
sitemap       = {}
internal_urls = {}
external_urls = {}
images        = {}


# create a subclass and override the handler methods
# now generates 2 lists for links and images that exist in page
#
class MyHTMLParser(HTMLParser):

	l_link = []
	l_img  = []

	def handle_starttag(self, tag, attrs):
		if tag == 'a' :
			attrs   = dict(attrs)
			self.l_link.append(attrs.get("href", ""))
		if tag == 'img' :
			attrs   = dict(attrs)
			# do not list the same images twice
			if attrs.get("src", "") not in self.l_img:
				self.l_img.append(attrs.get("src", ""))


# parses a url, populate the images and external_urls lists and return internal url list
#
def parse_url(url):
	global images
	global external_urls

	parser = MyHTMLParser()
	parser.l_link = []
	parser.l_img  = []

	response = urllib.urlopen(base_url+url);
	data =     response.read()
	parser.feed(data)
	
	urls          = split_urls(parser.l_link)

	external_urls[url] = urls[1]
	images[url]        = parser.l_img

	# return the internal urls
	return urls[0]


# split urls to internal and external
#
def split_urls(url_list) :
	internal_list = []
	external_list = []

	for url in url_list :
		if base_url in url and url not in internal_list and url != base_url:
			internal_list.append(url)
		elif url not in internal_list and url not in ['#','',base_url] and url.startswith('/#') == 0 :
			external_list.append(url)

	return [internal_list,external_list]


# parse recursively through urls
#
def generate_map(url) :
	for child_url in parse_url(url) :
		# exclude parent-child combinations in order to avoid infinite loop
		if [url,child_url] not in parsed_urls :
			parsed_urls.append([url,child_url])

			if url not in internal_urls:
				internal_urls[url] = list()
			internal_urls[url].append(child_url)
			parse(child_url)


# print the output
#
def print_map() :
	for key in internal_urls.keys():
		if key not in sitemap:
			sitemap[key] = {}
		sitemap[key]['internal_links'] = internal_urls[key]
		sitemap[key]['external_links'] = external_urls[key]
		sitemap[key]['images']         = images[key]

	pprint.pprint(sitemap)	


# main call
#

generate_map('')
print_map()

