from config.dbconfig import pg_config
import psycopg2

class UserDAO:

    def _init_(self):
        super().__init__()

    def getUserByUserId(self, user_id):
        return user_id

    def insert(self, firstname, lastname, date_birth, email, phone):
        user_id = 1
        return user_id

    def update(self, user_id, firstname, lastname, date_bith, email, phone):
        user_id = 1
        return user_id

    def delete(self, user_id):
        user_id = 1
        return user_id