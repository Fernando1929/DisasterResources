class LoginDAO:
    def __init__(self):
        super().__init__()

    # login = login_id, user_id, username, password

    # def getAllLogins(self):
    #     result = [[1,1, "juandelacalle", "password"]]
    #     return result

    def getLoginById(self, login_id):
        result = [1,1, "juandelacalle", "password"]
        return result

    def getLoginByUsername(self, username):
        result = [[1,1, "juandelacalle", "password"]]
        return result

    def getLoginByPassword(self, password):
        result = [[1,1, "juandelacalle", "password"]]
        return result

    def getLoginByUsernameAndPassword(self, username, password):
        result = [[1,1, "juandelacalle", "password"]]
        return result

    def getLoginByUserId(self, user_id):
        result = [[1,1, "juandelacalle", "password"]]
        return result

    def insert(self, user_id, username, password):
        login_id = 1
        return login_id

    def delete(self, login_id):
        return login_id

    def update(self, login_id, user_id, username, password):
        return login_id