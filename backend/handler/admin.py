from flask import jsonify
from dao.admin import AdminDAO
from dao.user import UserDAO
from dao.userPhone import UserPhoneDAO

class AdminHandler:

    def build_admin_attributes(self, user_id, admin_id, admin_firstname, admin_lastname, admin_date_birth, admin_email, admin_phone_id, admin_phone):
        result = {}
        result['admin_id'] = admin_id
        result['user_id'] = user_id
        result['admin_firstname'] = admin_firstname
        result['admin_lastname'] = admin_lastname
        result['admin_date_birth'] = admin_date_birth
        result['admin_email'] = admin_email
        result['admin_phone_id'] = admin_phone_id
        result['admin_phone'] = admin_phone
        return result

    def build_admin_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['admin_id'] = row[1]
        result['admin_firstname'] = row[2]
        result['admin_lastname'] = row[3]
        result['admin_date_birth'] = row[4]
        result['admin_email'] = row[5]
        result['admin_phone_id'] = row[6]
        result['admin_phone'] = row[7]
        return result

    def getAllAdmins(self):
        dao = AdminDAO()
        result = dao.getAllAdmins()
        result_list = []
        for row in result:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins = result_list)

    def getAdminById(self, admin_id):
        dao = AdminDAO()
        row = dao.getAdminById(admin_id)
        if not row:
            return jsonify(Error = "Admin Not Found"), 404
        else:
            admin = self.build_admin_dict(row)
            return jsonify(Admin = admin)

    def searchAdmins(self, args):
        admin_firstname = args.get("admin_firstname")
        admin_lastname = args.get("admin_lastname")
        admin_email = args.get('admin_email')
        admin_phone = args.get('admin_phone')
        admin_date_birth = args.get('admin_date_birth')
        dao = AdminDAO()
        admin_list = []
        if (len(args) == 2) and admin_firstname and admin_lastname:
            admin_list = dao.getAdminsByFirstnameAndLastname(admin_firstname , admin_lastname)
        elif (len(args) == 1) and admin_firstname:
            admin_list = dao.getAdminsByFirstname(admin_firstname)
        elif (len(args) == 1) and admin_lastname:
            admin_list = dao.getAdminsByLastname(admin_lastname)
        elif(len(args) == 1) and admin_email:
            admin_list = dao.getAdminsByEmail(admin_email)
        elif(len(args) == 1) and admin_phone:
            admin_list = dao.getAdminsByPhone(admin_phone)
        elif(len(args) == 1) and admin_date_birth:
            admin_list = dao.getAdminsByDateOfBirth(admin_date_birth)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins = result_list)

    def insertAdmin(self, json):
        admin_firstname = json['admin_firstname']
        admin_lastname = json['admin_lastname']
        admin_date_birth = json['admin_date_birth']
        admin_email = json['admin_email']
        admin_phone = json['admin_phone']

        if admin_firstname and admin_lastname and admin_date_birth and admin_email and admin_phone:
            dao_user = UserDAO()
            user_id = dao_user.insert(admin_firstname, admin_lastname, admin_date_birth, admin_email)
            dao_phone = UserPhoneDAO()
            admin_phone_id = dao_phone.insert(user_id, admin_phone)   
            dao_admin = AdminDAO()
            admin_id = dao_admin.insert(user_id)
            result = self.build_admin_attributes(user_id, admin_id, admin_firstname, admin_lastname, admin_date_birth, admin_email, admin_phone_id, admin_phone)
            return jsonify(Admin = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteAdmin(self, admin_id):
        dao_admin = AdminDAO()
        if not dao_admin.getAdminById(admin_id):
            return jsonify(Error = "Admin not found."), 404
        else:
            dao_user = UserDAO()
            user_id = dao_admin.delete(admin_id)
            dao_user.delete(user_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateAdmin(self, admin_id, json):
        dao_admin = AdminDAO()
        if not dao_admin.getAdminById(admin_id):
            return jsonify(Error = "Admin not found."), 404
        else:
            admin_firstname = json['admin_firstname']
            admin_lastname = json['admin_lastname']
            admin_date_birth = json['admin_date_birth']
            admin_email = json['admin_email']
            admin_phone = json['admin_phone']

            if admin_firstname and admin_lastname and admin_date_birth and admin_email and admin_phone:
                user_id = dao_admin.update(admin_id)
                dao_user = UserDAO()
                dao_user.update(user_id, admin_firstname, admin_lastname, admin_date_birth, admin_email, admin_phone)
                result = self.build_admin_attributes(user_id, admin_id, admin_firstname, admin_lastname, admin_date_birth, admin_email, admin_phone)
                return jsonify(Admin = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400
