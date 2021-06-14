import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}
for page in range(1, 10):
    data = {
        'cname': '',
        'pid': '',
        'keyword': '上海',
        'pageIndex': str(page),
        'pageSize': '10'
    }
    resp = requests.post(url=url, headers=headers, data=data)
    page_json = resp.json()
    for dic in page_json['Table1']:
        store_name = dic['storeName']
        addr = dic['addressDetail']
        print(store_name,addr)



