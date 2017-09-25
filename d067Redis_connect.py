import redis

r = redis.Redis(host='10.211.55.4', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))