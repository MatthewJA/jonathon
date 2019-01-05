"""Watch GitHub for events."""

import flask
from flask import request

from db import store, query


def webhook_push():
    # Store the push in the push log.
    data = request.json
    push = {
        'author': data['pusher']['name'],
        'time': data['repository']['pushed_at'],
        'time': data['repository']['pushed_at'],
    }
    pushes = query('pushes')
    pushes.append(push)
    store('pushes', pushes)

    # Pull the repo.
    result = subprocess.run([
        'git', 'clone', data['repository']['clone_url']])

    return 'ok' + repr(result)
