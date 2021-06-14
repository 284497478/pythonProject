import re
import urllib.request
import requests
import os

dir_name = 'ImgLibs'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}
# url = 'http://www.521609.com/tuku/mxxz/'
url = 'http://www.521609.com/qingchunmeinv/'
resp_text = requests.get(url=url, headers=headers).text
# ex = '<li style=.*?<img src="(.*?)" alt=.*?</li>'
ex = '<li>.*?<img src="(.*?)" width=.*?</li>'
# ex = '<img src=".*?(.*?)" alt=.*?'
img_src_list = re.findall(ex, resp_text, re.S)
for src in img_src_list:
    src = 'http://www.521609.com' + src
    print(src, '图片地址匹配成功！')
    img_path = dir_name + '/' + src.split('/')[-1]
    urllib.request.urlretrieve(src, img_path)
    print(img_path, '下载成功！！！')

# <li><a href="/qingchunmeinv/10535.html"><img src="/uploads/allimg/111019/11046303404-1-lp.jpg" width="160" height="220" border="0" alt="深圳山木培训吴玲"></a><br>
# <a href="/qingchunmeinv/10535.html" class="title">深圳山木培训吴玲</a></li>

# <li style="position: absolute; left: 0px; top: 0px;">
#     <a href="/tuku/1227.html" title="厦大校花程熙媛最新照片 又纯又欲你心动了吗?">
#         <img src="/d/file/p/2021/05-12/ef3b186417980c1729655690ed7bc8ff.jpg" alt="厦大校花程熙媛最新照片 又纯又欲你心动了吗?">
#         <p>厦大校花程熙媛最新照片 又纯又欲你心动了吗?</p>
#     </a>
# </li>
