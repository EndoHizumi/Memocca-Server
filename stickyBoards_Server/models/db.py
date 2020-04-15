import os
import dataset


def get_connection():
    user = os.getenv('STICKY_BOARDS_DB_ID')
    password = os.getenv('STICKY_BOARDS_DB_PASS')
    db_location = os.getenv('STICKY_BOARDS_DB_LOCATION')

    return dataset.connect(f'mysql://{user}:{password}@{db_location}/sticky_boards')
