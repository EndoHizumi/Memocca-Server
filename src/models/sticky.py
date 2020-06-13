import uuid

from cerberus import Validator
from flask import Blueprint, current_app, request

from . import db
from .io_util import set_response_json, validate_request

app = Blueprint('sticky', __name__)
sticky_db = db.get_connection()
stickies_table = sticky_db['stickies']

append_sticky_schema = {
    "user_id": {
        "type": "integer",
        "required": False,
    },
    "board_id": {
        "type": "string",
        "required": True,
        "maxlength": 6,
        "minlength": 6
    },
    "color_code": {
        "type": "integer",
        "required": True,
        "maxlength": 8,
        "minlength": 8
    },
    "text": {
        "type": "string",
        "required": False,
        "maxlength": 8000,
        "minlength": 0
    },
    "point_x": {
        "type": "integer",
        "required": False,
    },
    "point_y": {
        "type": "integer",
        "required": False,
    },
    "width": {
        "type": "integer",
        "required": False
    },
    "height": {
        "type": "integer",
        "required": False
    }
}


@app.route('/<board_id>', methods={'GET'})
def get_all_stickies(board_id):
    result = list(stickies_table.find(board_id=board_id))
    current_app.logger.debug(board_id)
    current_app.logger.debug(result)
    return set_response_json(data=result)


@app.route('/<board_id>', methods={'POST'})
def append_sticky(board_id):
    request_json = request.json
    result, message = validate_request(append_sticky_schema, request_json)
    if not result:
        return set_response_json(data={'reason': message}, message=f'validation failed. reason: {list(message.keys())}', status=400)

    sticky_id = stickies_table.count() + 1
    request_json.update({'sticky_id': sticky_id, 'board_id': board_id})
    stickies_table.insert(request_json)
    return set_response_json(data={"sticky_id": sticky_id})


@app.route('/<sticky_id>', methods={'PUT'})
def update_sticky(sticky_id):
    request_json = request.json
    request_json.update({'sticky_id': sticky_id})
    stickies_table.update(request_json, ['sticky_id'])
    return set_response_json(data=None)


@app.route('/<sticky_id>', methods={'DELETE'})
def delete_sticky(sticky_id):
    stickies_table.delete(sticky_id=sticky_id)
    return set_response_json(data=None)
