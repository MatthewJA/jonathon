from flask import Flask, request

app = Flask(__name__)

bens_global_state = {}


@app.route('/')
def recent_pushes():
    out = '<ul>'
    for push in bens_global_state.get('push', []):
        out += ('<li>{} @ {}</li>'.format(push['author'], push['time']))
    out += '</ul>'
    return out


if __name__ == '__main__':
    app.run()
