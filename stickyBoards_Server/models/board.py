import uuid
from datetime import datetime
import requests
from cerberus import Validator

get_board_info_schema = {
    "board_id": {
        "type": "string",
        "required": True,
        "maxlength": 128,
        "minlength": 128
    }
}
create_board_schema = {
    "board_name": {
        "type": "string",
        "required": True,
        "maxlength": 512,
        "minlength": 0
    },
    "owner_id": {
        "type": "string",
        "required": True,
        "maxlength": 32,
        "minlength": 0
    },
    "password": {
        "type": "string",
        "required": False,
        "maxlength": 255,
        "minlength": 0
    },
    "private": {
        "type": "integer",
        'allowed': [0, 1],
        "required": False,
        "max": 1,
        "min": 0
    },
}

update_board_schema = {
    "board_name": {
        "type": "string",
        "required": False,
        "maxlength": 512,
        "minlength": 0
    },
    "owner_id": {
        "type": "string",
        "required": False,
        "maxlength": 32,
        "minlength": 0
    },
    "password": {
        "type": "string",
        "required": False,
        "maxlength": 255,
        "minlength": 0
    },
    "private": {
        "type": "integer",
        'allowed': [0, 1],
        "required": False,
        "max": 1,
        "min": 0
    },
}

delete_board_schema = {
    "board_id": {
        "type": "string",
        "required": False,
        "maxlength": 128,
        "minlength": 128
    },
}

app = Blueprint('board', __name__)
sticky_db = db.get_connection()
board_table = sticky_db['boards']


@app.route('/', methods={'GET'})
def get_all_boards():
    # result = board_table.find(private=0)
    # data = [{'board_id': row['board_id'], 'board_name': row['board_name']} for row in result]
    # return set_response_json(data)
    pass

@app.route('/<board_id>', methods={'GET'})
def get_board_info(board_id):
    # result, message = validate_request(get_board_info_schema, {'board_id': board_id})
    # if not result:
    #     return set_response_json(data={'reason': message}, message=f'validation failed. reason: {list(message.keys())}', status=400)
    # result = list(board_table.find(board_id=board_id))
    # return set_response_json(result)
    pass


@app.route('/', methods={'POST'})
def create_board():
    request_json = request.json
    name = request_json['name']
    board_id = str(uuid.uuid4())[-6:]
    password = request_json['password']
    private = request_json.get('private', 1)
    user_id = ''
    board_table.insert({'board_id': board_id, 'board_name': name, 'password': password, 'private': private, 'owner_id': user_id})
    return set_response_json({'board_id': board_id, 'board_name': name})


@app.route('/<board_id>', methods={'PUT'})
def update_board(board_id):
    # request_json = request.json
    # old_table = requests.get(f"http://127.0.0.1:8080/board/{board_id}").json()
    # request_json.update({'board_id': board_id})
    # board_table.update(request_json, ['board_id'])
    # new_table = requests.get(f"http://127.0.0.1:8080/board/{board_id}").json()
    # return set_response_json({'board_id': board_id, 'changed': {'request': request.json, 'old': old_table['data'][0], 'new': new_table['data'][0]}})
    pass


@app.route('/<board_id>', methods={'DELETE'})
def delete_board(board_id):
    # old_table = requests.get(f"http://127.0.0.1:8080/board/{board_id}").json()
    # if len(old_table['data']) == 0:
    #     return set_response_json(data=None, message=f'board_id:{board_id} is not found', status=404)
    # board_table.delete(board_id=board_id)
    # new_table = requests.get(f"http://127.0.0.1:8080/board/{board_id}").json()
    # return set_response_json({'board_id': board_id, 'changed': {'request': {'board_id': board_id}, 'old': old_table['data'], 'new': new_table['data']}})
    pass


def set_id(board_name):
    id_raw = f'{board_name}{datetime.now()}'
    return hashlib.sha512(id_raw.encode()).hexdigest()


def set_response_json(data, message='', status=200):

    if str(status)[0:2] == '20':
        responce = {'status': 'success'}
    else:
        responce = {'status': 'failed', 'message': message}
    responce.update({'data': data})
    return jsonify(responce), status


def validate_request(schema, value):
    validator = Validator(schema)
    if not validator.validate(value):
        return False, validator.errors
    return True, None
