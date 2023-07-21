import datetime
import time
import redis


redis_host = '127.0.0.1'
redis_port = 6379 # default
channel = 'my_channel_1'

r = redis.Redis(host=redis_host, port=redis_port)

while True:
    message = "Hello. I'm a publisher 1. Time: %s" % datetime.datetime.now()
    r.publish(channel, message)
    time.sleep(1)