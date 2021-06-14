import requests

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}

data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}

resp = requests.post(url=url, headers=headers, data=data)
resp_json = resp.json()
for item in resp_json['list']:
    item_id = item['ID']
    item_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    item_data = {
        'id': item_id
    }
    item_resp = requests.post(url=item_url, headers=headers, data=item_data)
    item_resp_json = item_resp.json()
    eps_name = item_resp_json['epsName']
    eps_bln = item_resp_json['businessLicenseNumber']
    psn = item_resp_json['productSn']
    bp = item_resp_json['businessPerson']
    print(eps_name, eps_bln, psn, bp)
