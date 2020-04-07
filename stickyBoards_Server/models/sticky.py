from flask import Blueprint
from models import db

app = Blueprint('sticky', __name__)

@app.route('/', methods={'GET'})
def get_all_stickies():
    return ("sticky.get")

@app.route('/<sticky_id>', methods={'GET'})
def get_sticky_info(sticky_id):
    return ("sticky.get")

@app.route('/<sticky_id>', methods={'POST'})
def append_sticky(sticky_id):
    return ("sticky.post")


@app.route('/<sticky_id>', methods={'PUT'})
def update_sticky(sticky_id):
    return ("sticky.put")


@app.route('/<sticky_id>', methods={'DELETE'})
def delete_sticky(sticky_id):
    return ("sticky.delete")
