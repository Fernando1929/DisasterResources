from flask import jsonify
from dao.customer import CustomerDAO

class CustomerHandler:
    def build_customer_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['user_firstname'] = row[1]
        result['user_lasname'] = row[2]
        result['user_date_birth'] = row[3]
        result['user_email'] = row[4]
        result['user_phone'] = row[5]
        result['customer_id'] = row[6]
        return result

    def build_customer_attributes(self, user_id, user_firstname, user_lastname, user_date_birth, user_email, user_phone, customer_id):
        result = {}
        result['user_id'] = user_id
        result['user_firstname'] = user_firstname
        result['user_lasname'] = user_lastname
        result['user_date_birth'] = user_date_birth
        result['user_email'] = user_email
        result['user_phone'] = user_phone
        result['customer_id'] = customer_id
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
        firstname = args.get("firstname")
        lastname = args.get("lastname")
        email = args.get("email")
        dao = CustomerDAO()
        customers_list = []
        if (len(args) == 2) and firstname and lastname:
            customers_list = dao.getCustomerByFirstnameAndLastname(firstname, lastname)
        elif (len(args) == 1) and firstname:
            customers_list = dao.getCustomerByFirstname(firstname)
        elif (len(args) == 1) and lastname:
            customers_list = dao.getCustomerByLastname(lastname)
        elif (len(args) == 1) and email:
            customers_list = dao.getCustomerByEmail(email)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in customers_list:
            result = self.build_customer_dict(row)
            result_list.append(result)
        return jsonify(Customer=result_list)

def insertCustomer(self, json):
    firstname = json['firstname']
    lastname = json['lastname']
    date_birth = json['date_birth']
    email = json['email']
    phone = json['phone']
    if firstname and lastname and date_birth and email and phone:
        # dao = UserDAO()
        # user_id = dao.insert(firstname, lastname, date_birth, email, phone) 
        user_id = 1;          
        dao = CustomerDAO()
        customer_id = dao.insert(user_id)
        result = self.build_customer_attributes(user_id, firstname, lastname, date_birth, email, phone, customer_id)
        return jsonify(Customer = result), 201
    else:
        return jsonify(Error = "Unexpected attributes in post request"), 400

def updateCustomer(self, customer_id, form):
    customer_dao = CustomerDAO()
    if not customer_dao.getCustomerById(customer_id):
        return jsonify(Error = "Customer not found."), 404
    else:
        if len(form) != 5:
            return jsonify(Error = "Malformed update request."), 404
        else:
            firstname = form["firstname"]
            lastname = form["lastname"]
            date_bith = form["date_birth"]
            email = form["email"]
            phone = form["phone"]
            if firstname and lastname and date_bith and email and phone:
                user_id = customer_dao.update(customer_id)
                #user_dao = UserDAO()
                #user_dao.update(user_id, firstname, lastname, date_bith, email, phone)
                result = self.build_customer_attributes(user_id, firstname, lastname, date_bith, email, phone, customer_id)
                return jsonify(Customer = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

def deleteCustomer(self, customer_id):
    customer_dao = CustomerDAO()
    if not customer_dao.getCustomerById(customer_id):
        return jsonify(Error = "Customer not found."), 404
    else:
        user_id = customer_dao.delete(customer_id)
        #user_dao = UserDAO()
        #user_dao.delete(user_id)
        return jsonify(DeleteStatus = "OK"), 200
        

