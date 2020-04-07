from flask import Flask, request, redirect, jsonify
from models.board import app as board_app

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(board_app, url_prefix='/board')

@app.route('/', methods={'GET'})
def hello():
    return ('hello')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
