from flask import Flask, request

import watchathon
from db import query, clear_all

app = Flask(__name__)


@app.route('/')
def recent_pushes():
    out = '<ul>'
    pushes = query('pushes')
    for push in pushes:
        out += ('<li>{} @ {}</li>'.format(push['author'], push['time']))
    out += '</ul>'
    return out


push_hook = app.route('/push_hook', methods=['POST'])(watchathon.webhook_push)

app.route('/clear_all')
def clear_db():
    clear_all()
    return 'Cleared'


if __name__ == '__main__':
    app.run(debug=True)
