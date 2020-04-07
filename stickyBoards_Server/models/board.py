from flask import Blueprint
from models import db

app = Blueprint('board', __name__)

@app.route('/', methods={'GET'})
def get():
    return ("board.get")

@app.route('/<board_id>', methods={'GET'})
def get2():
    return ("board.get")

@app.route('/<board_id>', methods={'POST'})
def post(board_id):
    return ("board.post")


@app.route('/<board_id>', methods={'PUT'})
def put(board_id):
    return ("board.put")


@app.route('/<board_id>', methods={'DELETE'})
def delete(board_id):
    return ("board.delete")
