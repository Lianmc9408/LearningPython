#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-16 上午10:01


# http://blog.csdn.net/damotiansheng/article/details/44338411
# 并发聊天服务器，可以多人聊天
import socketserver


# 使用socketserver模块必须定义一个类继承socketserver.XXX，并重写父类的handle()方法
# 除了handle()方法，还有setup()[准备工作]，finish()[结束工作]方法
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('服务端启动')
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf-8'))
                print('waiting....')
                inp = input('>>>')
                conn.sendall(bytes(inp, 'utf-8'))
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)
    server.serve_forever()
