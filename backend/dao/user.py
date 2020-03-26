class UserDAO:
    def __init__(self):
        super().__init__()

    def getUserByUserId(self, user_id):
        result = [1, "Alex", "Smith", "03/03/1996", "alexsmith@gmail.com", "7870007777"]
        return result

    def insert(self, firstname, lastname, date_birth, email, phone):
        user_id = 1
        return user_id

    def update(self, user_id, firstname, lastname, date_bith, email, phone):
        return user_id

    def delete(self, user_id):
        return user_id