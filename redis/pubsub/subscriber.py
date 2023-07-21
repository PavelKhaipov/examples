import redis
import time


redis_host = '127.0.0.1'
redis_port = 6379 # default
channels = ['my_channel_1', 'my_channel_2']

while True:
    r = redis.Redis(host=redis_host, port=redis_port, socket_timeout=5)
    p = r.pubsub()
    p.subscribe(channels)

    try:
        while True:
            for message in p.listen():
                if message['type'] == 'message':
                    data = message['data'].decode()
                    channel = message['channel']
                    print("[%s] %s" % (channel, data))

    except:
        print("Connection failed.")
        time.sleep(10)
        print("Try to connect to Redis host...")
