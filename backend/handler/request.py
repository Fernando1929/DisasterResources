from flask import jsonify
from dao.request import RequestDAO
from dao.customer import CustomerDAO
from dao.requestCategory import RequestCategoryDAO

class RequestHandler:

    def build_request_dict(self, row, resources):
        result = {}
        result['request_id'] = row[0]
        result['customer_id'] = row[1]
        result['request_title'] = row[2]
        result['request_date'] = row[3]
        result['request_description'] = row[4]
        result['request_status'] = row[5]
        result['resources'] = resources
        return result

    def build_request_attributes(self, request_id, customer_id, request_title, request_date, request_description, request_status, resources):
        result = {}
        result['request_id'] = request_id
        result['customer_id'] = customer_id 
        result['request_title'] = request_title
        result['request_date'] = request_date
        result['request_status'] = request_status
        result['request_description'] = request_description
        result['resources'] = resources
        return result

    def build_resources_dict(self, row):
        result = {}
        result['category_id'] = row[0]
        result['category_name'] = row[1]
        result['request_quantity'] = row[2]
        return result

    def fixDict(self, request_list):
        result_list = []
        resources_list = []
        index = 1
        for row in request_list:
            if index < len(request_list) and row[0] == request_list[index][0]:
                resources_list.append(row[6:])
            else:
                resources_list.append(row[6:])
                result = self.build_request_dict(row[:6], self.createResourceDict(resources_list))
                result_list.append(result)
                resources_list.clear()
            index += 1
        return result_list

    def createResourceDict(self, resources_list):
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return result_list
    
    def getAllRequests(self):
        dao = RequestDAO()
        request_list = dao.getAllRequests()
        result_list = self.fixDict(request_list)
        return jsonify(Requests = result_list)

    def getRequestById(self, request_id):
        dao = RequestDAO()
        row = dao.getRequestById(request_id)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            request = self.fixDict(row)
            return jsonify(Request = request)

    def getRequestsByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            request_list = []
            request_dao = RequestDAO()
            request_list = request_dao.getRequestsByCustomerId(customer_id)
            result_list = self.fixDict(request_list)
            return jsonify(Requests = result_list)

    def searchRequests(self, args):
        request_title = args.get("request_title")
        request_status = args.get("request_status")
        category_name = args.get("category_name")
        dao = RequestDAO()
        request_list = []
        if (len(args) == 1) and request_title:
            request_list = dao.getRequestsByTitle(request_title)
        elif (len(args) == 1) and request_status:
            request_list = dao.getRequestsByStatus(request_status)
        elif (len(args) == 1) and category_name:
            request_list = dao.getRequestsByCategoryName(category_name)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = self.fixDict(request_list)
        return jsonify(Requests = result_list)

    def insertRequest(self, json):
        customer_id = json["customer_id"]
        request_title = json["request_title"]
        request_date = json["request_date"]
        request_description = json["request_description"]
        request_status = "Pending"
        resources = json["resources"]

        if customer_id and request_title and request_date and request_status and request_description and resources:
            request_dao = RequestDAO()
            request_category_dao = RequestCategoryDAO()
            request_id = request_dao.insert(customer_id, request_title, request_date, request_description, request_status)
            for item in resources:
                request_category_dao.insert(request_id, item["category_id"], item["request_quantity"])
            result = self.build_request_attributes(request_id, customer_id, request_title, request_date, request_description, request_status, resources)
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
            request_date = json["request_date"]
            request_description = json["request_description"]
            request_status = "Pending"
            resources = json["resources"]

            if customer_id and request_title and request_date and request_status and request_description and resources:
                request_dao = RequestDAO()
                request_category_dao = RequestCategoryDAO()
                request_id = request_dao.update(request_id, customer_id, request_title, request_date, request_status, request_description)
                for item in resources:
                    request_category_dao.update(request_id, item["category_id"], item["request_quantity"])
                result = self.build_request_attributes(request_id, customer_id, request_title, request_date, request_status, request_description)
                return jsonify(Request = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteRequest(self, request_id):
        request_dao = RequestDAO()
        request_category_dao = RequestCategoryDAO()
        if not request_dao.getRequestById(request_id):
            return jsonify(Error = "Request not found."), 404
        else:
            request_category_dao.delete(request_id)
            request_dao.delete(request_id)
            return jsonify(DeleteStatus = "OK"), 200