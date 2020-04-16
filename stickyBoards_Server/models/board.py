from flask import Blueprint, jsonify
from models import db

app = Blueprint('board', __name__)
sticky_db = db.get_connection()
board_table = sticky_db['boards']


@app.route('/', methods={'GET'})
def get_all_boards():
    board_table = sticky_db['boards']
    result = board_table.find(private=0)
    data = [{'board_id': row['board_id'], 'board_name': row['board_name']} for row in result]
    return set_response_json(data)


@app.route('/<board_id>', methods={'GET'})
def get_board_info(board_id):
    board_table = sticky_db['boards']
    result = board_table.find(board_id=board_id)
    return set_response_json(list(result))


@app.route('/<board_id>', methods={'POST'})
def create_board(name, password, private):
    return ("board.post")


@app.route('/<board_id>', methods={'PUT'})
def update_board(board_id):
    return ("board.put")


@app.route('/<board_id>', methods={'DELETE'})
def delete_board(board_id):
    return ("board.delete")

def set_response_json(data, message=''):

    if len(message) == 0:
        responce = {'status': 'success'}
    else:
        responce = {'status': 'failed', 'message': message}
    responce.update({'data': data})
    return jsonify(responce)
