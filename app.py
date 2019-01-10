from flask import Flask, request, jsonify

from db import db


app = Flask(__name__)

@app.route('/usegit', methods=['POST'])
def slack_use_git():
    return 'yeah'

@app.route('/pushes', methods=['POST'])
def slack_pushes():
    return ','.join([i['author'] for i in db.query('pushes')])

@app.route('/push', methods=['POST'])
def github_push():
    data = request.json
    push = {
        'author': data['pusher']['name'],
        'time': data['repository']['pushed_at'],
        'time': data['repository']['pushed_at'],
    }

    # Store the push in the push log.
    pushes = query('pushes')
    pushes.append(push)
    store('pushes', pushes)

    return 'ok' + repr(result)


if __name__ == '__main__':
    app.run(debug=True)
