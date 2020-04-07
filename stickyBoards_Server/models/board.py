import dataset
import ..src.main.app

class board:

    def __init__(self):
        user = env['sticky_db_user']
        password = env['sticky_db_password']
        db_location = env['sticky_db_location']

        self.db = dataset.connect(f'mysql://{user}:{password}@{db_location}/board')

    @app.route('board/<board_id>', methods={'GET'})
    def get(board_id):
        pass


    def post(board_id):
        pass


    def put(board_id):
        pass


    def delete(board_id):
        pass
