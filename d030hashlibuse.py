#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-8 下午10:41


import hashlib

m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest())  # 8b1a9953c4611296a827abf8c47804d7
m.update(b"It's me")
print(m.hexdigest())  # 5ddeb47b2f925ad0bf249c52e342728a，为HelloIt's me的MD5
m1 = hashlib.md5()
m1.update(b"HelloIt's me")
print(m.hexdigest())  # 5ddeb47b2f925ad0bf249c52e342728a，为HelloIt's me的MD5

# ######## md5 ########
hash = hashlib.md5()
# help(hash.update)hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
print(hash.digest())

# ######## sha256 ########
hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha384 ########
hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########
hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# 对加密算法中添加自定义key再来做加密
hash = hashlib.md5(bytes('898oaFs09f', encoding="utf-8"))
hash.update(bytes('admin', encoding="utf-8"))
print(hash.hexdigest())
