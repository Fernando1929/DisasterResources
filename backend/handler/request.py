from flask import jsonify
from dao.request import RequestDAO
from dao.customer import CustomerDAO

class RequestHandler:

    def build_request_dict(self, row):
        result = {}
        result['request_id'] = row[0]
        result['customer_id'] = row[1]
        result['request_title'] = row[2]
        result['request_quantity'] = row[3]
        result['request_date'] = row[4]
        return result

    def build_request_attributes(self, request_id, customer_id, request_title, request_quantity, request_date):
        result = {}
        result['request_id'] = request_id
        result['customer_id'] = customer_id 
        result['request_title'] = request_title
        result['request_quantity'] = request_quantity
        result['request_date'] = request_date
        return result

    def getAllRequests(self):
        dao = RequestDAO()
        request_list = dao.getAllRequests()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def getRequestById(self, request_id):
        dao = RequestDAO()
        row = dao.getRequestById(request_id)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            request = self.build_request_dict(row)
            return jsonify(Request = request)

    def getRequestsByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            request_list = []
            result_list = []
            request_dao = RequestDAO()
            request_list = request_dao.getRequestsByCustomerId(customer_id)
            for row in request_list:
                result = self.build_request_dict(row)
                result_list.append(result)
            return jsonify(Requests = result_list)

    def searchRequests(self, args):
        request_title = args.get("request_title")
        dao = RequestDAO()
        request_list = []
        if (len(args) == 1) and request_title:
            request_list = dao.getRequestsByTitle(request_title)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def insertRequest(self, json):
        customer_id = json["customer_id"]
        request_title = json["request_title"]
        request_quantity = json["request_quantity"]
        request_date = json["request_date"]

        if customer_id and request_title and request_quantity and request_date:
            request_dao = RequestDAO()
            request_id = request_dao.insert(customer_id, request_title, request_quantity, request_date)
            result = self.build_request_attributes(request_id, customer_id, request_title, request_quantity, request_date)
            return jsonify(Request = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateRequest(self, request_id, json):
        request_dao = RequestDAO()
        if not request_dao.getRequestById(request_id):
            return jsonify(Error = "Request not found."), 404
        else:
            customer_id = json["customer_id"]
            request_title = json["request_title"]
            request_quantity = json["request_quantity"]
            request_date = json["request_date"]
            
            if customer_id and request_title and request_quantity and request_date:
                request_dao = RequestDAO()
                request_id = request_dao.update(request_id, customer_id, request_title, request_quantity, request_date)
                result = self.build_request_attributes(request_id, customer_id, request_title, request_quantity, request_date)
                return jsonify(Request = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteRequest(self, request_id):
        request_dao = RequestDAO()
        if not request_dao.getRequestById(request_id):
            return jsonify(Error = "request not found."), 404
        else:
            request_dao.delete(request_id)
            return jsonify(DeleteStatus = "OK"), 200