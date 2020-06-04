import os
import redis
import sys

from flask import Flask


r = redis.StrictRedis(host='redis', decode_responses=True, port=6379)
APP = Flask(__name__)


@APP.route('/')
def index():
    print('Received request on index!', file=sys.stderr)
    desired_channel = os.environ['REDIS_CHANNEL']
    print(f'Env: "REDIS_CHANNEL" is: {desired_channel}', file=sys.stderr)
    
    r.publish(desired_channel, 'Hello Shukuji')

    print('Message published on channel!', file=sys.stderr)

    return 'Hello NeelShukuji - Request completed'
