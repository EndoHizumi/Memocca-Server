from flask import Blueprint
from . import db

app = Blueprint('user', __name__)


@app.route('/<board_id>', methods={'GET'})
def get_all_users(board_id):
    return ("user.get")


@app.route('/<user_id>', methods={'GET'})
def get_user_info(user_id):
    return ("user.get")


@app.route('/<user_id>', methods={'POST'})
def register_user_info(user_id):
    return ("user.post")


@app.route('/<user_id>', methods={'PUT'})
def update_user_info(user_id):
    return ("user.put")


@app.route('/<user_id>', methods={'DELETE'})
def delete_user_info(user_id):
    return ("user.delete")
