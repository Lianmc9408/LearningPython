from wsgiref.simple_server import make_server


def f1(environ):
    data = '<h1>hello f1</h1>'
    return [data.encode('utf8')]


def f2(environ):
    data = '<h1>hello f2</h1>'
    return [data.encode('utf8')]


def routers():
    urlpath = (
        ('/f1', f1),
        ('/f2', f2),
    )
    return urlpath


def application(environ, start_response):
    # 通过environ封装成一个所有请求信息（请求头+请求体）的对象，environ是一个包含所有HTTP请求信息的dict对象
    # start_response 一个发送HTTP响应的函数，可以很方便的设置相应头
    # ('Content-Type', 'text/html')元祖组成响应头的键值对
    # print('environ', environ['PATH_INFO'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if path == item[0]:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ['<h1>404</h1>'.encode('utf-8')]
        # if path == '/f1':
        #     return f1(environ)
        # elif path == '/f2':
        #     return f2(environ)
        # return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 8080, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
