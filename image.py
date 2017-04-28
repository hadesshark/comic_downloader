# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys
import wget

url = "https://i.nhentai.net/galleries/1011875/42.jpg"

headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}
