import json
import os

import redis

db = redis.from_url(os.environ.get('REDIS_URL'))


def query(key):
    return json.loads(db.get(key))


def store(key, value):
    db.append(key, json.dumps(value))
