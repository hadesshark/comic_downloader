# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys

url = "https://nhentai.net/g/182867/"

headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}

page = requests.get(url, headers)
page_con_encode = page.text.encode('utf-8')

print(page_con_encode)
