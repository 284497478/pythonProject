import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}
main_url = 'https://xueqiu.com'

session = requests.Session()
session.get(url=main_url, headers=headers)

url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=216065&size=15'
page_text = session.get(url=url, headers=headers).json()
print(page_text)
