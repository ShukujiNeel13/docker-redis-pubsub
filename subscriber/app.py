import os
import redis

r = redis.StrictRedis(host='redis', decode_responses=True, port=6379)


def listen_on_channel():
    desired_channel = os.environ['REDIS_CHANNEL']
    print(f'"REDIS_CHANNEL" is: {desired_channel}')
    p = r.pubsub()
    print('Redis pubsub instance created')

    try:
        p.subscribe(**{desired_channel: handle_message})
    except ConnectionError as err:
        print('ConnectionError in redis.pubsub.subscribe operation. Error obj is:\n')
        print(err)
    else:
        print('Subscribe to channel complete. Listening for messages...')
        return p.run_in_thread(sleep_time=0.001)
    

def handle_message(msg_obj: dict):
    print('Received message on channel!')
    print('-'*9)
    print('\nMessage object received is:')
    from pprint import pformat
    print(pformat(msg_obj))

    print('\nPlease check this object, can you read the channel name?')

    msg_string = msg_obj['data']
    print('Extracted "data" from message object as:')
    print(msg_string)


if __name__ == '__main__':
    print('Starting subscriber app...')
    listen_on_channel()
