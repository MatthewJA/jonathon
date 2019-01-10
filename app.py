from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/git')
def use_git():
    return 'yeah'


if __name__ == '__main__':
    app.run(debug=True)
