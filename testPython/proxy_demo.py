import random

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}
url = 'https://www.xicidaili.com/nn'
ips = []
'''
    代理ip池的形式
    dic = {
        'https':291.1.1.1:8080
    }
    http_proxy.append(dic)
'''
http_proxy=[] #代理池

page_text = requests.get(url=url, headers=headers, proxies=random.choice(http_proxy)).text
