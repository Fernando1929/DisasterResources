from flask import jsonify
from dao.creditCard import CreditCardDAO
from dao.payment import PaymentDAO
from dao.customer import CustomerDAO

class CreditCardHandler:

    def build_creditcard_dict(self, row):
        result = {}
        result['creditcard_id'] = row[0]
        result['payment_id'] = row[1]
        result['customer_id'] = row[2]
        result['creditcard_name'] = row[3]
        result['creditcard_number'] = row[4]
        result['creditcard_ccv'] = row[5]
        result['creditcard_exp_date'] = row[6]
        return result

    def build_creditcard_attributes(self, creditcard_id, payment_id, customer_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date):
        result = {}
        result['creditcard_id'] = creditcard_id
        result['payment_id'] = payment_id
        result['customer_id'] = customer_id
        result['creditcard_name'] = creditcard_name
        result['creditcard_number'] = creditcard_number
        result['creditcard_ccv'] = creditcard_ccv
        result['creditcard_exp_date'] = creditcard_exp_date
        return result

    def getAllCreditCard(self):
        dao = CreditCardDAO()
        creditcard_list = dao.getAllCreditCard()
        result_list = []
        for row in creditcard_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(CreditCard = result_list)

    def getCreditCardById(self, creditcard_id):
        dao = CreditCardDAO()
        row = dao.getCreditCardById(creditcard_id)
        if not row:
            return jsonify(Error = "Credit Card Not Found"), 404
        else:
            creditcard = self.build_creditcard_dict(row)
            return jsonify(CreditCard = creditcard)

    def searchCreditCard(self, args):
        creditcard_name = args.get("creditcard_name")
        creditcard_number = args.get("creditcard_number")
        dao = CreditCardDAO()
        creditcard_list = []
        if (len(args) == 1) and creditcard_name:
            creditcard_list = dao.getCreditCardByName(creditcard_name)
        elif (len(args) == 1) and creditcard_number:
            creditcard_list = dao.getCreditCardByNumber(creditcard_number)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in creditcard_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(CreditCard = result_list)

    def getCreditCardByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else :
            dao = CreditCardDAO()
            row = dao.getCreditCardByCustomerId(customer_id)
            if not row:
                return jsonify(Error = "Credit Card Not Found"), 404
            else:
                creditcard = self.build_creditcard_dict(row)
                return jsonify(CreditCard = creditcard)

    def insertCreditCard(self, json):
        customer_id = json["customer_id"]
        creditcard_name = json["creditcard_name"]
        creditcard_number = json["creditcard_number"]
        creditcard_ccv = json["creditcard_ccv"]
        creditcard_exp_date = json["creditcard_exp_date"]
        if customer_id and creditcard_name and creditcard_number and creditcard_ccv and creditcard_exp_date:
            payment_dao = PaymentDAO()
            payment_id = payment_dao.insert(customer_id)
            creditcard_dao = CreditCardDAO()
            creditcard_id = creditcard_dao.insert(payment_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date)
            result = self.build_creditcard_attributes(creditcard_id, payment_id, customer_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date)
            return jsonify(CreditCard = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400
    
    def updateCreditCard(self, creditcard_id, json):
        creditcard_dao = CreditCardDAO()
        if not creditcard_dao.getCreditCardById(creditcard_id):
            return jsonify(Error = "Credit Card not found."), 404
        else:
            customer_id = json["customer_id"]
            creditcard_name = json["creditcard_name"]
            creditcard_number = json["creditcard_number"]
            creditcard_ccv = json["creditcard_ccv"]
            creditcard_exp_date = json["creditcard_exp_date"]
            if customer_id and creditcard_name and creditcard_number and creditcard_ccv and creditcard_exp_date:
                payment_id = creditcard_dao.update(creditcard_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date)
                payment_dao = PaymentDAO()
                payment_dao.update(payment_id, customer_id)
                result = self.build_creditcard_attributes(creditcard_id, payment_id, customer_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date)
                return jsonify(CreditCard = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteCreditCard(self, creditcard_id):
        creditcard_dao = CreditCardDAO()
        if not creditcard_dao.getCreditCardById(creditcard_id):
            return jsonify(Error = "Credit Card not found."), 404
        else:
            payment_id = creditcard_dao.delete(creditcard_id)
            payment_dao = PaymentDAO()
            payment_dao.delete(payment_id)
            return jsonify(DeleteStatus = "OK"), 200