from flask import Blueprint, jsonify, request
from models import db
import hashlib
from datetime import datetime

app = Blueprint('board', __name__)
sticky_db = db.get_connection()
board_table = sticky_db['boards']


@app.route('/', methods={'GET'})
def get_all_boards():
    result = board_table.find(private=0)
    data = [{'board_id': row['board_id'], 'board_name': row['board_name']} for row in result]
    return set_response_json(data)


@app.route('/<board_id>', methods={'GET'})
def get_board_info(board_id):
    result = board_table.find(board_id=board_id)
    return set_response_json(list(result))


@app.route('/', methods={'POST'})
def create_board():
    request_json = request.json
    name = request_json['name']
    board_id = set_id(name)
    password = request_json['password']
    private = request_json.get('private', 1)
    user_id = ''
    board_table.insert({'board_id': board_id, 'board_name': name, 'password': password, 'private': private, 'owner_id': user_id})
    return set_response_json({'board_id': board_id, 'board_name': name})


@app.route('/<board_id>', methods={'PUT'})
def update_board(board_id):
    return ("board.put")


@app.route('/<board_id>', methods={'DELETE'})
def delete_board(board_id):
    return ("board.delete")


def set_id(board_name):
    id_raw = f'{board_name}{datetime.now()}'
    return hashlib.sha256(id_raw.encode()).hexdigest()


def set_response_json(data, message='', status=200):

    if str(status)[0:2] == '20':
        responce = {'status': 'success'}
    else:
        responce = {'status': 'failed', 'message': message}
    responce.update({'data': data})
    return jsonify(responce), status

