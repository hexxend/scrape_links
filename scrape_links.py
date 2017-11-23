#!/usr/bin/env python
# Scrapes all links off a page and returns them in a list
#
# 10/24/2017
# hexxend
#

import requests
from lxml import html
import os
from sys import platform
from sys import argv


# Check what platform we are running on
if platform == 'linux' or platform == 'darwin':
    clear = 'clear'
elif platform == 'win32':
    clear = 'cls'

try:
    url = argv[1]
    if url[:7] != 'http://' or url[:7] != 'https://':
        url = 'http://' + url
        #print('not a valid URL (did you include http:// or https://?)')
    def get_parsed_page(url):
       
        sess = requests.Session()
        r0 = sess.get(url)
        parsed_page = html.fromstring(r0.content)
        os.system(clear)
        print('Generating link list for %s' % url)
        hrefs = parsed_page.xpath('//a')
        print('\nHeader: \n',r0.headers, '\n', '\nStatus: ', r0.status_code, '\n')

        for href in hrefs:
            links = []
            links = [href.attrib['href']]
            print(links)

    get_parsed_page(url)

except IndexError:
	print('Usage: %0 example.com\nScrapes the specified url for links')		  



