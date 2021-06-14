import requests
from bs4 import BeautifulSoup

fp = open('./sanguo.text', 'w', encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36 '
}
main_url = 'http://shicimingju.com/book/sanguoyanyi.html'

resp = requests.get(url=main_url, headers=headers)
resp.encoding = 'utf-8'
page_text = resp.text
soup = BeautifulSoup(page_text, 'lxml')
chapter_list = soup.select('.book-mulu a')
for chapter in chapter_list:
    title = chapter.string
    detail_url = 'http://www.shicimingju.com' + chapter['href']
    page_text_detail_resp = requests.get(url=detail_url, headers=headers)
    page_text_detail_resp.encoding = 'utf-8'
    page_text_detail = page_text_detail_resp.text
    soup = BeautifulSoup(page_text_detail, 'lxml')
    div_tag = soup.find('div', class_='chapter_content')
    content = div_tag.text
    fp.write(title + ':' + content + '\n')
    print(title, '保存成功')
fp.close()
