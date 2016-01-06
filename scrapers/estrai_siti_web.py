# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

URL_PAGE= 'http://www.ancitel.it/link/siti/sitiweb_reply.cfm?val_start=%s&comune=&id_area=&id_regione=&id_provincia=00&popolazione_da=&popolazione_a=';
TOT_PAGES = 319;
ITEM_FOR_PAGE = 25

print "provincia;citta;web"

for i in range(1, TOT_PAGES + 1):
    url = URL_PAGE % (1 + (ITEM_FOR_PAGE * (i-1)))
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text)
        tables = soup.findAll('table')
        for tr in tables[5].findAll('tr'):
            tds = tr.findAll('td')
            for td in tds:
                provincia = td.get_text().strip()
                if len(provincia) == 2:                     
                    try:
                        citta =  td.next_sibling.next_sibling.get_text().strip()
                        url =  td.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip()
                        print "%s;%s;%s" %(provincia, citta, url)
                    except Exception as e:
                        pass