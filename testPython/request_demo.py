import requests

#
# url = 'https://www.sogou.com'
#
# resp = requests.get(url=url)
#
# page_text = resp.text
#
# with open('./sougou.html', 'w', encoding='utf-8') as fp:
#     fp.write(page_text)

keyword = input('enter akey word')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}
params = {
    'query': keyword
}
url = 'https://www.sogou.com/web'
resp = requests.get(url=url, params=params, headers=headers)
resp.encoding = 'utf-8'
page_text = resp.text
fileName = keyword + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName, '爬取完毕！！！')
