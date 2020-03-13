from flask import jsonify
from dao.customer import CustomerDAO
from dao.user import UserDAO

class CustomerHandler:
    def build_customer_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['customer_id'] = row[1]
        result['customer_firstname'] = row[2]
        result['customer_lastname'] = row[3]
        result['customer_date_birth'] = row[4]
        result['customer_email'] = row[5]
        result['customer_phone'] = row[6]
        return result

    def build_customer_attributes(self, user_id, customer_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone):
        result = {}
        result['user_id'] = user_id
        result['customer_id'] = customer_id
        result['customer_firstname'] = customer_firstname
        result['customer_lastname'] = customer_lastname
        result['customer_date_birth'] = customer_date_birth
        result['customer_email'] = customer_email
        result['customer_phone'] = customer_phone
        return result

    def getAllCustomer(self):
        dao = CustomerDAO()
        customers_list = dao.getAllCustomer()
        result_list = []
        for row in customers_list:
            result = self.build_customer_dict(row)
            result_list.append(result)
        return jsonify(Customers = result_list)

    def getCustomerById(self, customer_id):
        dao = CustomerDAO()
        row = dao.getCustomerById(customer_id)
        if not row:
            return jsonify(Error = "Customer Not Found"), 404
        else:
            customer = self.build_customer_dict(row)
            return jsonify(Customer = customer)

    def searchCustomer(self, args):
        customer_firstname = args.get("customer_firstname")
        customer_lastname = args.get("customer_lastname")
        customer_email = args.get("customer_email")
        dao = CustomerDAO()
        customers_list = []
        if (len(args) == 2) and customer_firstname and customer_lastname:
            customers_list = dao.getCustomerByFirstnameAndLastname(customer_firstname, customer_lastname)
        elif (len(args) == 1) and customer_firstname:
            customers_list = dao.getCustomerByFirstname(customer_firstname)
        elif (len(args) == 1) and customer_lastname:
            customers_list = dao.getCustomerByLastname(customer_lastname)
        elif (len(args) == 1) and customer_email:
            customers_list = dao.getCustomerByEmail(customer_email)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in customers_list:
            result = self.build_customer_dict(row)
            result_list.append(result)
        return jsonify(Customer=result_list)

    def insertCustomer(self, json):
        customer_firstname = json['customer_firstname']
        customer_lastname = json['customer_lastname']
        customer_date_birth = json['customer_date_birth']
        customer_email = json['customer_email']
        customer_phone = json['customer_phone']
        if customer_firstname and customer_lastname and customer_date_birth and customer_email and customer_phone:
            user_dao = UserDAO()
            user_id = user_dao.insert(customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)          
            customer_dao = CustomerDAO()
            customer_id = customer_dao.insert(user_id)
            result = self.build_customer_attributes(user_id, customer_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)
            return jsonify(Customer = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateCustomer(self, customer_id, json):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            print(json)
            customer_firstname = json["customer_firstname"]
            customer_lastname = json["customer_lastname"]
            customer_date_birth = json["customer_date_birth"]
            customer_email = json["customer_email"]
            customer_phone = json["customer_phone"]
            if customer_firstname and customer_lastname and customer_date_birth and customer_email and customer_phone:
                user_id = customer_dao.update(customer_id)
                user_dao = UserDAO()
                user_dao.update(user_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)
                result = self.build_customer_attributes(user_id, customer_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)
                return jsonify(Customer = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteCustomer(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            user_id = customer_dao.delete(customer_id)
            user_dao = UserDAO()
            user_dao.delete(user_id)
            return jsonify(DeleteStatus = "OK"), 200