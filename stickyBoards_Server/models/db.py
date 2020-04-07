import os
import dataset


class db:

    def get_connection(self):
        user = os.getenv['sticky_db_user']
        password = os.getenv['sticky_db_password']
        db_location = os.getenv['sticky_db_location']

        return dataset.connect(f'mysql://{user}:{password}@{db_location}/board')