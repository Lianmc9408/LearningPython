import os
import requests
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
from html.parser import unescape
import pymysql
from hashlib import md5
from multiprocessing import Pool


def get_page_index(offset, keyword):
    url = 'https://www.toutiao.com/search_content/?'
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
    }
    try:
        response = requests.get(url, params)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None


def parse_page_detail(detail, url):
    soup = BeautifulSoup(detail, 'lxml')
    head = soup.select('body')[0].get_text()
    parttern = re.compile("var BASE_DATA = .*?articleInfo.*?content: '(.*?);',\s*groupId", re.S)
    xml = re.search(parttern, head)
    if xml:
        htmlr = unescape(xml.group(1))
        soup1 = BeautifulSoup(htmlr, 'lxml')
        img_list = soup1.find_all('img')
        title = img_list[0].attrs['alt']
        img_url_list = []
        for img_url in img_list:
            img_url_list.append(img_url.attrs['src'])
            # download_image(img_url.attrs['src'])
        return {
            'title': title,
            'url': url,
            'images': img_url_list
        }


def save_to_mysql(result):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='124578', db='t1')
    # cursor = conn.cursor()
    conn.set_charset('utf8')
    cursor = conn.cursor()
    # ...'title': title,
    #         'url': url,
    #         'images': img_url_list
    title1 = result.get('title')
    cursor.execute('insert into artical(title) VALUE (%s)', title1)
    a = conn.insert_id()
    images_list = result.get('images')
    for image_url in images_list:
        cursor.execute('insert into image_url(url) values(%s)', image_url)
        c = conn.insert_id()
        cursor.execute('insert into art_to_image(artical_id,images_id) VALUE (%s, %s)', (a, c))

    conn.commit()
    cursor.close()
    conn.close()


def download_image(url):
    try:
        print('正在下载', url)
        response = requests.get(url)
        if response.status_code == 200:
            file_path = '{0}/{1}/{2}.{3}'.format(os.getcwd(), 'toutiaoimages', md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
    except RequestException:
        print('下载图片出错', url)


def main(offset):
    html = get_page_index(offset, '街拍')
    for url in parse_page_index(html):
        if url:
            detail = get_page_detail(url)
            if detail:
                result = parse_page_detail(detail, url)
                if result:
                    # print(result)
                    save_to_mysql(result)


if __name__ == '__main__':
    # main()
    groups = [i * 20 for i in range(1)]
    pool = Pool()
    pool.map(main, groups)
