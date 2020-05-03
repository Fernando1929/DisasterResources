from flask import jsonify
from dao.athMovil import AthMovilDAO
from dao.payment import PaymentDAO
from dao.customer import CustomerDAO

class AthMovilHandler:

    def build_athMovil_dict(self, row):
        result = {}
        result['payment_id'] = row[0]
        result['ath_movil_id'] = row[1]
        result['ath_movil_phone'] = row[2]
        result['customer_id'] = row[3]
        return result

    def build_athMovil_attributes(self, ath_movil_id, payment_id, customer_id, ath_movil_phone):
        result = {}
        result['ath_movil_id'] = ath_movil_id
        result['payment_id'] = payment_id
        result['customer_id'] = customer_id
        result['ath_movil_phone'] = ath_movil_phone
        return result

    def getAllAthMovil(self):
        dao = AthMovilDAO()
        ath_movil_list = dao.getAllAthMovil()
        result_list = []
        for row in ath_movil_list:
            result = self.build_athMovil_dict(row)
            result_list.append(result)
        return jsonify(AthMovil = result_list)

    def getAthMovilById(self, ath_movil_id):
        dao = AthMovilDAO()
        row = dao.getAthMovilById(ath_movil_id)
        if not row:
            return jsonify(Error = "Ath Movil Not Found"), 404
        else:
            ath_movil = self.build_athMovil_dict(row)
            return jsonify(AthMovil = ath_movil)

    def searchAthMovil(self, args):
        ath_movil_phone = args.get("ath_movil_phone")
        dao = AthMovilDAO()
        ath_movil_list = []
        if (len(args) == 1) and ath_movil_phone:
            ath_movil_list = dao.getAthMovilByPhone(ath_movil_phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in ath_movil_list:
            result = self.build_athMovil_dict(row)
            result_list.append(result)
        return jsonify(AthMovil = result_list)

    def getAthMovilByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            dao = AthMovilDAO()
            row = dao.getAthMovilByCustomerId(customer_id)
            if not row:
                return jsonify(Error = "Ath Movil Not Found"), 404
            else:
                ath_movil = self.build_athMovil_dict(row)
                return jsonify(AthMovil = ath_movil)

    def insertAthMovil(self, json):
        customer_id = json["customer_id"]
        ath_movil_phone = json["ath_movil_phone"]
        
        if customer_id and ath_movil_phone:
            payment_dao = PaymentDAO()
            payment_id = payment_dao.insert(customer_id)
            ath_movil_dao = AthMovilDAO()
            ath_movil_id = ath_movil_dao.insert(payment_id, ath_movil_phone)
            result = self.build_athMovil_attributes(ath_movil_id, payment_id, customer_id, ath_movil_phone)
            return jsonify(AthMovil = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400
    
    def updateAthMovil(self, ath_movil_id, json):
        ath_movil_dao = AthMovilDAO()
        if not ath_movil_dao.getAthMovilById(ath_movil_id):
            return jsonify(Error = "Ath Movil not found."), 404
        else:
            customer_id = json["customer_id"]
            ath_movil_phone = json["ath_movil_phone"]
            if customer_id and ath_movil_phone:
                payment_id = ath_movil_dao.update(ath_movil_id, ath_movil_phone)
                payment_dao = PaymentDAO()
                payment_dao.update(payment_id, customer_id)
                result = self.build_athMovil_attributes(ath_movil_id, payment_id, customer_id, ath_movil_phone)
                return jsonify(AthMovil = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteAthMovil(self, ath_movil_id):
        ath_movil_dao = AthMovilDAO()
        if not ath_movil_dao.getAthMovilById(ath_movil_id):
            return jsonify(Error = "Ath Movil not found."), 404
        else:
            payment_id = ath_movil_dao.delete(ath_movil_id)
            payment_dao = PaymentDAO()
            payment_dao.delete(payment_id)
            return jsonify(DeleteStatus = "OK"), 200