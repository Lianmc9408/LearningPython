import redis

pool = redis.ConnectionPool(host='10.211.55.4', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print(r.get('foo'))