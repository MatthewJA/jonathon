from flask import Flask, request

import watchathon

app = Flask(__name__)

bens_global_state = {}


@app.route('/')
def recent_pushes():
    out = '<ul>'
    for push in bens_global_state.get('push', []):
        out += ('<li>{} @ {}</li>'.format(push['author'], push['time']))
    out += '</ul>'
    return out


app.route('/push_hook')(watchathon.webhook_push)


if __name__ == '__main__':
    app.run()
