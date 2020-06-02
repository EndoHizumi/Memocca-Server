from cerberus import Validator
from flask import jsonify


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
