import requests
import os
from lxml import etree

dir_name = 'zhanzhangsucai'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}

url = 'https://sc.chinaz.com/tupian/rentiyishu_%d.html'

for page in range(1, 2):
    if page == 1:
        new_url = 'https://sc.chinaz.com/tupian/rentiyishu.html'
    else:
        new_url = format(url % page)

    resp = requests.get(url=new_url, headers=headers)
    resp.encoding = 'utf-8'
    page_text = resp.text
    html_tree = etree.HTML(page_text)
    img_div_list = html_tree.xpath('//*[@id="container"]/div')
    for img_div in img_div_list:
        title = img_div.xpath('.//img/@alt')[0]
        scr_path = 'http:' + img_div.xpath('.//img/@src2')[0]
        img_data = requests.get(url=scr_path, headers=headers).content
        img_save_path = dir_name + '/' + title + '.jpg'
        with open(img_save_path, 'wb') as fp:
            fp.write(img_data)
            print(title, '保存成功！！')
