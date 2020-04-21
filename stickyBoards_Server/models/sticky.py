from flask import Blueprint, request, current_app
from models import db
from models.io_util import set_response_json, validate_request
import uuid

app = Blueprint('sticky', __name__)
sticky_db = db.get_connection()
stickies_table = sticky_db['stickies']


@app.route('/<board_id>', methods={'GET'})
def get_all_stickies(board_id):
    result = list(stickies_table.find(board_id=board_id))
    current_app.logger.debug(board_id)
    current_app.logger.debug(result)
    return set_response_json(data=result)


@app.route('/<board_id>', methods={'POST'})
def append_sticky(board_id):
    request_json = request.json
    sticky_id = str(uuid.uuid4()).split("-")[-1]
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