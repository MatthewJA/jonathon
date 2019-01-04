"""Watch GitHub for events."""

import flask
from flask import request

bens_global_state = {}


def webhook_push():
    data = request.json
    push = {
        'author': data['pusher']['name'],
        'time': data['repository']['pushed_at'],
    }
    if 'pushes' in bens_global_state:
        bens_global_state['pushes'].append(push)
    else:
        bens_global_state['pushes'] = [push]
    return 'changed ben\'s global state: added ' + repr(
        bens_global_state['pushes'][-1])
