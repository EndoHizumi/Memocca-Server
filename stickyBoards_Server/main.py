from flask import Flask, request, redirect, jsonify
from models.board import app as board_app
from models.sticky import app as sticky_app
from models.user import app as user_app

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(board_app, url_prefix='/board')
app.register_blueprint(sticky_app, url_prefix='/sticky')
app.register_blueprint(user_app, url_prefix='/user')

@app.route('/', methods={'GET'})
def hello():
    return ('hello')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
