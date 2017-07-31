# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os

url = "https://nhentai.net/g/202549/"

headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-encoding':
        'gzip'}

page = requests.get(url, headers)
page_con_encode = page.text.encode('utf-8')

# 確定可以抓取
# print(page_con_encode)
__xpath_for_title = u"//div[@id='info']/h2//text()"
__xpath_for_images = u"//div[@class='thumb-container']/a[@class='gallerythumb']/img/@data-src"
page_ready_to_xpath = etree.HTML(page_con_encode)

temp_title = page_ready_to_xpath.xpath(__xpath_for_title)
temp_images_list = page_ready_to_xpath.xpath(__xpath_for_images)

# 顯示檔案名稱是否存在
# print(os.listdir('./download/'))
# 有抓到圖片 url
# print(temp_images_list)

if not temp_title[0] in os.listdir('./download'):

    print(temp_title[0])
    file_save_string = './download/' + temp_title[0]
    if not os.path.exists(file_save_string):
        os.makedirs(file_save_string)

    # 直接計算數量
    num_images = len(temp_images_list)
    # 抓取用網址重要數字
    url_num = temp_images_list[1].split('/')[-2]
    print(url_num)

    # 出現關於不同格式圖片的問題
    for item in range(num_images):
        print(item + 1)

        # print(temp_images_list[item].split('.')[-1])
        kind_of_image_file = '.' + temp_images_list[item].split('.')[-1]

        temp_url = r"https://i.nhentai.net/galleries/" + str(url_num) + '/'

        file_name_or_download_name = str(item + 1) + kind_of_image_file

        print(temp_url + str(item + 1) + '.jpg')
        with open(file_save_string + '/' + file_name_or_download_name, 'wb') as outf:
            data = requests.get(temp_url + file_name_or_download_name)
            # print(data.status_code)
            print(temp_url + file_name_or_download_name)
            if data.status_code == 200:
                outf.write(data.content)
else:
    print("{0} 存在！！".format(temp_title[0]))
