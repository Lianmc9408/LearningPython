import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool
import gevent

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print('Exception', e)
        return None


def page_parse(html):
    parttern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?">(.*?)</a.*?'
                          + 'star">(.*?)</p.*?releasetime">(.*?)</p>.*?integer">(.*?)</i.*?fraction">(\d+)</i>.*?</dd>',
                          re.S)
    items = re.findall(parttern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],  # 去掉"主演："这三个字符
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in page_parse(html):
        write_to_file(item)


if __name__ == '__main__':
    # for i in range(10):
    #     main(i * 10)
    # 进程池
    # pool = Pool()
    # pool.map(main, [i * 10 for i in range(10)])
    # 携程
    gevent.joinall([
            gevent.spawn(main, i * 10) for i in range(10)]
    )
