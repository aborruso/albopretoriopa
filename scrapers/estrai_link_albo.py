# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import csv
import os
import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool
import requests


def link_albo_pretorio(tag):
    prog = re.compile("^albo pretorio$", re.I)
    return tag.name == 'a' and prog.match(tag.get_text().strip())

def link_albo_online(tag):
    prog = re.compile("^albo online$", re.I)
    return tag.name == 'a' and prog.match(tag.get_text().strip())

def link_albo_online_trattino(tag):
    prog = re.compile("^albo on\-line$", re.I)
    return tag.name == 'a' and prog.match(tag.get_text().strip())

def link_albo_generico(tag):
    prog = re.compile(".*albo\s.*", re.I)
    return tag.name == 'a' and prog.match(tag.get_text().strip())


def analyze_response(row):
    try:
        url = row['web']
        provincia = row['provincia']
        citta = row['citta']
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url,  headers = user_agent, timeout = 20, allow_redirects=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text)
            albo = find_albo(soup)
            if albo != None:
                link = albo.get('href')
                if not link.startswith('http'):
                    link = urljoin(url, link)
                print "%s;%s;%s;%s;%s;%s" % (provincia, citta, url, response.status_code, response.url, link)
        else:
            print "%s;%s;%s;%s;ANOMALIA" % (provincia, citta, url, response.status_code)
    except Exception as e:
        print "%s;%s;%s;ANOMALIA;%s" % (provincia, citta, url, str(e))
        

def find_albo(soup):
    result = soup.find(link_albo_pretorio)
    if result != None:
        return result

    result = soup.find(link_albo_online)
    if result != None:
        return result

    result = soup.find(link_albo_online_trattino)
    if result != None:
        return result
    
    result = soup.find(link_albo_generico)
    if result != None:
        return result
    
    return None


with open('siti-web.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    pool = Pool(30)
    for row in reader:
        pool.spawn(analyze_response, row)