from urllib import request
url_ip = 'http://httpbin.org/ip'
# url_ip = 'http://127.0.0.1:8000/host'


def use_simple_urllib():
    response = request.urlopen(url_ip)
    # print(response.read)
    print(response.info())
    print(response.read().decode('utf8'))


if __name__ == '__main__':
    use_simple_urllib()
