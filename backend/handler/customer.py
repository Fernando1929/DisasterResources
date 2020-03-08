from flask import jsonify
from dao.customer import CustomerDAO

class CustomerHandler:
    def build_customer_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['customer_firstname'] = row[1]
        result['customer_lasname'] = row[2]
        result['customer_date_birth'] = row[3]
        result['customer_email'] = row[4]
        result['customer_phone'] = row[5]
        result['customer_id'] = row[6]
        return result

    def build_customer_attributes(self, user_id, firstname, lastname, date_birth, email, phone, customer_id):
        result = {}
        result['user_id'] = user_id
        result['customer_firstname'] = firstname
        result['customer_lasname'] = lastname
        result['customer_date_birth'] = date_birth
        result['customer_email'] = email
        result['customer_phone'] = phone
        result['customer_id'] = customer_id
        return result

    def getAllCustomers(self):
        dao = CustomerDAO()
        customers_list = dao.getAllCustomers()
        result_list = []
        for row in customers_list:
            result = self.build_customer_dict(row)
            result_list.append(result)
        return jsonify(Customers=result_list)

    def getCustomerById(self, customer_id):
        dao = CustomerDAO()
        row = dao.getCustomerById(customer_id)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
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

def insertCustomer(self, form):
    if len(form) != 5:
        return jsonify(Error = "Malformed post request"), 400
    else: 
        firstname = form['firstname']
        lastname = form['lastname']
        date_birth = form['date_birth']
        email = form['email']
        phone = form['phone']
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

def insertCustomerJson(self, json):
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