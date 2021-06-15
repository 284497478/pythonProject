from multiprocessing.dummy import Pool
import requests
import time

urls = [
    "http://127.0.0.1:5000/test1",
    "http://127.0.0.1:5000/test2",
    "http://127.0.0.1:5000/test3"
]


def get_requests(url):
    page_text = requests.get(url).text
    return len(page_text)


if __name__ == "__main__":
    start = time.time()
    pool = Pool(3)
    result_list = pool.map(get_requests, urls)
    print(result_list)
    print('总耗时：', time.time() - start)
