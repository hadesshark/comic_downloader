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

# 確定可以抓取
# print(page_con_encode)

__xpath_for_images = u"//div[@class='thumb-container']/a[@class='gallerythumb']/img/@data-src"
page_ready_to_xpath = etree.HTML(page_con_encode)
temp_images_list = page_ready_to_xpath.xpath(__xpath_for_images)
print(temp_images_list)