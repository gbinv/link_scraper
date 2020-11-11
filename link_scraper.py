#!/usr/bin/env python

"""	Linktr.ee Link Scraper
   	Author: Brendan Burke @gbinv (http://github.com/gbinv/) 
   	Description: Checks Linktr.ee for a given username & scrapes links. Prints to screen and csv  
"""
import sys
import os
import requests
import csv
import random
from bs4 import BeautifulSoup

os.system('clear')
# Class for colors stolen from Micah Hoffman (@WebBreacher)
#

class Colors:
	YELLOW = "\033[93m"
	RED = "\033[91m"
	GREEN = "\033[92m"
	ENDC = "\033[0m"


# print coloured messages, also stolen from Micah Hoffman (@WebBreacher)
def error(msg):
    print(Colors.RED + msg + Colors.ENDC)
def positive(msg):
    print(Colors.GREEN + msg + Colors.ENDC)

#print a banner
print("Linktr.ee Scraper")
print("Author: @gbinv (http://github.com/gbinv/)\n")
user = input("Username:")

#get response. had to include ua because linktree hates bots :( Adapted in 1.4 from osi.ig  by @th3unkn0n
url = 'https://www.linktr.ee/%s' %user

useragent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7']

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': random.choice(useragent),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'www.google.com',
    'Connection': 'keep-alive',
}

r = requests.get(url, headers=headers)

#check if user is valid and exit if not
if r.status_code == 200:
	positive('User found!\n')
elif r.status_code == 404:
	error('Username Not Found. Exiting.')
	exit()
print("Saving links to " '%s_linktree.csv' %user)
print("\n")
#make soup
data = r.text
soup = BeautifulSoup(data, features="html.parser")

#print to csv and name it after user
f = csv.writer(open('%s_linktree.csv' %user, 'w'))
f.writerow(['Found On Linktr.ee'])
link_list = soup.find_all('a')
for link in link_list:
    links = link.get('href')
# Add each link to a row
    f.writerow([links])
# print results to screen    
    print(Colors.GREEN, link.get('href'))
    
