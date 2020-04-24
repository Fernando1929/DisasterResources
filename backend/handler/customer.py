from flask import jsonify
from dao.customer import CustomerDAO
from dao.user import UserDAO
from dao.userPhone import UserPhoneDAO

class CustomerHandler:
    
    def build_customer_dict(self, row):
        result = {}
        result['customer_id'] = row[0]
        result['user_id'] = row[1]
        result['customer_firstname'] = row[2]
        result['customer_lastname'] = row[3]
        result['customer_date_birth'] = row[4]
        result['customer_email'] = row[5]
        result['customer_phone'] = row[7]
        return result

    def build_customer_attributes(self, customer_id, user_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone):
        result = {}
        result['customer_id'] = customer_id
        result['user_id'] = user_id
        result['customer_firstname'] = customer_firstname
        result['customer_lastname'] = customer_lastname
        result['customer_date_birth'] = customer_date_birth
        result['customer_email'] = customer_email
        result['customer_phone'] = customer_phone
        return result

    def getAllCustomers(self):
        dao = CustomerDAO()
        customers_list = dao.getAllCustomers()
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

    def searchCustomers(self, args):
        customer_firstname = args.get("customer_firstname")
        customer_lastname = args.get("customer_lastname")
        customer_email = args.get("customer_email")
        customer_phone = args.get("customer_phone")
        customer_date_birth = args.get("customer_date_birth")
        dao = CustomerDAO()
        customers_list = []
        if (len(args) == 2) and customer_firstname and customer_lastname:
            customers_list = dao.getCustomersByFirstnameAndLastname(customer_firstname, customer_lastname)
        elif (len(args) == 1) and customer_firstname:
            customers_list = dao.getCustomersByFirstname(customer_firstname)
        elif (len(args) == 1) and customer_lastname:
            customers_list = dao.getCustomersByLastname(customer_lastname)
        elif (len(args) == 1) and customer_email:
            customers_list = dao.getCustomersByEmail(customer_email)
        elif (len(args) == 1) and customer_phone:
            customers_list = dao.getCustomersByPhone(customer_phone)
        elif (len(args) == 1) and customer_date_birth:
            customers_list = dao.getCustomersByDateOfBirth(customer_date_birth)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in customers_list:
            result = self.build_customer_dict(row)
            result_list.append(result)
        return jsonify(Customers = result_list)

    def insertCustomer(self, json):
        customer_firstname = json['customer_firstname']
        customer_lastname = json['customer_lastname']
        customer_date_birth = json['customer_date_birth']
        customer_email = json['customer_email']
        customer_phone = json['customer_phone']

        if customer_firstname and customer_lastname and customer_date_birth and customer_email and customer_phone:
            user_dao = UserDAO()
            user_id = user_dao.insert(customer_firstname, customer_lastname, customer_date_birth, customer_email)
            dao_phone = UserPhoneDAO()
            dao_phone.insert(user_id, customer_phone)         
            customer_dao = CustomerDAO()
            customer_id = customer_dao.insert(user_id)
            result = self.build_customer_attributes(customer_id, user_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)
            return jsonify(Customer = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateCustomer(self, customer_id, json):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            customer_firstname = json["customer_firstname"]
            customer_lastname = json["customer_lastname"]
            customer_date_birth = json["customer_date_birth"]
            customer_email = json["customer_email"]
            customer_phone = json["customer_phone"]
            
            if customer_firstname and customer_lastname and customer_date_birth and customer_email and customer_phone:
                user_id = customer_dao.update(customer_id)
                user_dao = UserDAO()
                user_dao.update(user_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)
                result = self.build_customer_attributes(customer_id, user_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone)
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