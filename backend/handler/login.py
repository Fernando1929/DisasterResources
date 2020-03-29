from flask import jsonify
from dao.login import LoginDAO
from dao.user import UserDAO

class LoginHandler:

    def build_login_dict(self, row):
        result = {}
        result['login_id'] = row[0]
        result['user_id'] = row[1]
        result['username'] = row[2]
        result['password'] = row[3]
        return result

    def build_login_attributes(self, login_id, user_id, username, password):
        result = {}
        result['login_id'] = login_id
        result['user_id'] = user_id
        result['username'] = username
        result['password'] = password
        return result

    def getAllLogins(self):
        dao = LoginDAO()
        login_list = dao.getAllLogins()
        result_list = []
        for row in login_list:
            result = self.build_login_dict(row)
            result_list.append(result)
        return jsonify(Logins = result_list)

    def getLoginById(self, login_id):
        dao = LoginDAO()
        row = dao.getLoginById(login_id)
        if not row:
            return jsonify(Error = "Login Not Found"), 404
        else:
            login = self.build_login_dict(row)
            return jsonify(Login = login)

    def getLoginByUserId(self, user_id):
        user_dao = UserDAO()
        if not user_dao.getUserById(user_id):
            return jsonify(Error = "User not found."), 404
        else:
            login_list = []
            result_list = []
            dao = LoginDAO()
            login_list = dao.getLoginByUserId(user_id)
            # if not address_list:
            #     return jsonify(Error = "Address Not Found"), 404
            # else:
            for row in login_list:
                result = self.build_login_dict(row)
                result_list.append(result)
            return jsonify(Login = result_list)

    # def searchLogin(self, args):
    #     username = args.get("username")
    #     password = args.get("password")

    #     dao = LoginDAO()
    #     login_list = []
    #     if (len(args) == 1) and username:
    #         login_list = dao.getLoginByUsername(city)
    #     elif (len(args) == 1) and password:
    #         login_list = dao.getLoginByPassword(state_province)
    #     elif (len(args) == 2) and username and password:
    #         login_list = dao.getLoginByUsernameAndPassword(city, country)
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in login_list:
    #         result = self.build_login_dict(row)
    #         result_list.append(result)
    #     return jsonify(Login = result_list)

    def insertLogin(self, json):
        user_id = json["user_id"]
        username = json["username"]
        password = json["password"]

        if user_id and username and password:
            login_dao = LoginDAO()
            login_id = login_dao.insert(user_id, username, password)
            result = self.build_login_attributes(login_id, user_id, username, password)
            return jsonify(Login = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateLogin(self, login_id, json):
        login_dao = LoginDAO()
        if not login_dao.getLoginById(login_id):
            return jsonify(Error = "Login not found."), 404
        else:
            user_id = json["user_id"]
            username = json["username"]
            password = json["password"]

            if user_id and username and password:
                login_dao = LoginDAO()
                login_id = login_dao.update(login_id, user_id, username, password)
                result = self.build_login_attributes(login_id, user_id, username, password)
                return jsonify(Login = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteLogin(self, login_id):
        login_dao = LoginDAO()
        if not login_dao.getLoginById(login_id):
            return jsonify(Error = "Login not found."), 404
        else:
            login_dao.delete(login_id)
            return jsonify(DeleteStatus = "OK"), 200