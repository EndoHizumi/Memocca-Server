from flask import Flask, request, Response, stream_with_context
from flask_sse import sse
from models.board import app as board_app
from models.sticky import app as sticky_app
from models.user import app as user_app
from models import db, io_util
from time import sleep
from datetime import datetime


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config["REDIS_URL"] = "redis://sticky_sse_queue"
app.register_blueprint(sse, url_prefix='/stream')
app.register_blueprint(board_app, url_prefix='/board')
app.register_blueprint(sticky_app, url_prefix='/sticky')
app.register_blueprint(user_app, url_prefix='/user')


@app.route('/', methods={'GET'})
def hello():
    with open('index.html') as f:
        return f.read()


@app.route('/<board_id>', methods={'GET'})
def return_client(board_id):
    with open('sse_client.html') as f:
        return f.read()


@app.route('/sse/<board_id>', methods={'GET'})
def start_stream(board_id):
    con = db.get_connection()
    stream_table = con['stream']
    last_event_id = request.headers.get('Last-Event-Id', 0)
    sse.publish(list(stream_table.find(last_event_id=last_event_id)), channel=board_id)
    return io_util.set_response_json(data='message send!!')


@app.before_request
def authorize():
    app.logger.debug(f'request.path:{request.path}')
    app.logger.debug(f'request.path.split:{request.path.split("/")[1].strip()}')
    is_access_token = len(request.cookies.get('accesstoken', '')) != 0
    skip_auth_page = request.path.split('/')[1] in ['', 'index.html', 'auth', '.png', '.jpg', '.gif', 'favicon.ico']
    app.logger.debug(f'is_access_token:{is_access_token}/skip_auth_page:{skip_auth_page}')
    if not is_access_token and not skip_auth_page:
        return io_util.set_response_json(data=None, message='not authorize', status=401)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
