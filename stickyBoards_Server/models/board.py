from flask import Blueprint
from models import db

app = Blueprint('board', __name__)

@app.route('/', methods={'GET'})
def get_all_boards():
    return ("board.get")

@app.route('/<board_id>', methods={'GET'})
def get_board_info():
    return ("board.get")

@app.route('/<board_id>', methods={'POST'})
def create_board(board_id):
    return ("board.post")


@app.route('/<board_id>', methods={'PUT'})
def update_board(board_id):
    return ("board.put")


@app.route('/<board_id>', methods={'DELETE'})
def delete_board(board_id):
    return ("board.delete")
