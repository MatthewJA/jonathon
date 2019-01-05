"""Watch GitHub for events."""

import flask
from flask import request

from db import store, query


def webhook_push():
    data = request.json
    push = {
        'author': data['pusher']['name'],
        'time': data['repository']['pushed_at'],
    }
    pushes = query('pushes')
    pushes.append(push)
    store('pushes', pushes)
    return 'ok'
