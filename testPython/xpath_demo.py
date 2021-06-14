import requests
from lxml import etree
import os

dir_name = 'GirlsLib'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}

url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
for page in range(1, 6):
    if page == 1:
        new_url = 'http://pic.netbian.com/4kmeinv/'
    else:
        new_url = format(url % page)
    resp = requests.get(url=new_url, headers=headers)
    resp.encoding = 'gbk'
    page_text = resp.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        title = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = dir_name + '/' + title
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(title, '保存成功！！！')
