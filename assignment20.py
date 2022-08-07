# 9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
# python -m pip install redis
import redis
conn = redis.Redis()
conn.hset('test1',{'count':1,'name':'Fester Bestertester'})
conn.hgetall('test1')


# 10. Increment the count field of test and print it.
conn.hincrby('test', 'count', 1)
conn.hget('test', 'count')