import redis

r = redis.Redis(
    host='redis-17036.crce178.ap-east-1-1.ec2.redns.redis-cloud.com',
    port=17036,
    decode_responses=True,
    username="default",
    password="aEFyUNcb1N6sYOPYKygLUWsckEMmlofM",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

