#!/usr/bin/env python
# Scrapes all links off a page and returns them in a list
#
# 10/24/2017
#
# Requires python3.x, requests, and lxml
#
#Copyright (C) 2019  HexXend
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#hexxend@protonmail.com

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



