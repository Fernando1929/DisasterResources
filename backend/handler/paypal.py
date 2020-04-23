from flask import jsonify
from dao.paypal import PaypalDAO
from dao.payment import PaymentDAO
from dao.customer import CustomerDAO

class PaypalHandler:

    def build_paypal_dict(self, row):
        result = {}
        result['paypal_id'] = row[0]
        result['payment_id'] = row[1]
        result['customer_id'] = row[2]
        result['paypal_username'] = row[3]
        result['paypal_password'] = row[4]
        return result

    def build_paypal_attributes(self, paypal_id, payment_id, customer_id, paypal_username, paypal_password):
        result = {}
        result['paypal_id'] = paypal_id
        result['payment_id'] = payment_id
        result['customer_id'] = customer_id
        result['paypal_username'] = paypal_username
        result['paypal_password'] = paypal_password
        return result

    def getAllPaypal(self):
        dao = PaypalDAO()
        paypal_list = dao.getAllPaypal()
        result_list = []
        for row in paypal_list:
            result = self.build_paypal_dict(row)
            result_list.append(result)
        return jsonify(Paypal = result_list)

    def getPaypalById(self, paypal_id):
        dao = PaypalDAO()
        row = dao.getPaypalById(paypal_id)
        if not row:
            return jsonify(Error = "Paypal Not Found"), 404
        else:
            paypal = self.build_paypal_dict(row)
            return jsonify(AthMovil = paypal)

    def searchPaypal(self, args):
        paypal_username = args.get("paypal_username")
        dao = PaypalDAO()
        paypal_list = []
        if (len(args) == 1) and paypal_username:
            paypal_list = dao.getPaypalByUsername(paypal_username)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in paypal_list:
            result = self.build_paypal_dict(row)
            result_list.append(result)
        return jsonify(Paypal = result_list)

    def getPaypalByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else :
            dao = PaypalDAO()
            row = dao.getPaypalByCustomerId(customer_id)
            if not row:
                return jsonify(Error = "Paypal Not Found"), 404
            else:
                paypal = self.build_paypal_dict(row)
                return jsonify(AthMovil = paypal)

    def insertPaypal(self, json):
        customer_id = json["customer_id"]
        paypal_username = json["paypal_username"]
        paypal_password = json["paypal_password"]
        
        if customer_id and paypal_username and paypal_password:
            payment_dao = PaymentDAO()
            payment_id = payment_dao.insert(customer_id)
            paypal_dao = PaypalDAO()
            paypal_id = paypal_dao.insert(payment_id, paypal_username, paypal_password)
            result = self.build_paypal_attributes(paypal_id, payment_id, customer_id, paypal_username, paypal_password)
            return jsonify(Paypal = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400
    
    def updatePaypal(self, paypal_id, json):
        paypal_dao = PaypalDAO()
        if not paypal_dao.getPaypalById(paypal_id):
            return jsonify(Error = "Paypal not found."), 404
        else:
            customer_id = json["customer_id"]
            paypal_username = json["paypal_username"]
            paypal_password = json["paypal_password"]

            if customer_id and paypal_username and paypal_password:
                payment_id = paypal_dao.update(paypal_id, paypal_username, paypal_password)
                payment_dao = PaymentDAO()
                payment_dao.update(payment_id, customer_id)
                result = self.build_paypal_attributes(paypal_id, payment_id, customer_id, paypal_username, paypal_password)
                return jsonify(Paypal = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def deletePaypal(self, paypal_id):
        paypal_dao = PaypalDAO()
        if not paypal_dao.getPaypalById(paypal_id):
            return jsonify(Error = "Paypal not found."), 404
        else:
            payment_id = paypal_dao.delete(paypal_id)
            payment_dao = PaymentDAO()
            payment_dao.delete(payment_id)
            return jsonify(DeleteStatus = "OK"), 200