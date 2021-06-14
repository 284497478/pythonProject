import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}

url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': 5,
    'interval_id': '100:90',
    'action': '',
    'start': 10,
    'limit': 10
}
resp = requests.get(url=url, params=params, headers=headers)
page_text = resp.json()
for movie in page_text:
    name = movie['title']
    score = movie['score']
    print(name, score)