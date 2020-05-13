from flask import jsonify
from dao.reservation import ReservationDAO
from dao.resourceReservation import ResourceReservationDAO
from dao.customer import CustomerDAO
from dao.request import RequestDAO
from handler.resource import ResourceHandler

class ReservationHandler:

    def build_reservation_dict(self, row, resources):
        result = {}
        result['reservation_id'] = row[0]
        result['customer_id'] = row[1]
        result['request_id'] = row[2]
        result['reservation_date'] = row[3]
        result['reservation_status'] = row[4]
        result['resources'] = resources
        return result

    def build_reservation_attributes(self, reservation_id, customer_id, request_id, reservation_date, reservation_status, resources):
        result = {}
        result['reservation_id'] = reservation_id
        result['customer_id'] = customer_id
        result['request_id'] = request_id
        result['reservation_date'] = reservation_date
        result['reservation_status'] = reservation_status
        result['resources'] = resources
        return result

    def build_resources_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['resource_name'] = row[1]
        result['reservation_quantity'] = row[2]
        return result

    def fixDict(self, reservation_list):
        result_list = []
        resources_list = []
        index = 1
        for row in reservation_list:
            if index < len(reservation_list) and row[0] == reservation_list[index][0]:
                resources_list.append(row[5:])
            else:
                resources_list.append(row[5:])
                result = self.build_reservation_dict(row[:5], self.createResourceDict(resources_list))
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

    def getAllReservations(self):
        dao = ReservationDAO()
        reservation_list = dao.getAllReservations()
        result_list = self.fixDict(reservation_list)
        return jsonify(Reservations = result_list)

    def getReservationById(self, reservation_id):
        dao = ReservationDAO()
        row = dao.getReservationById(reservation_id)
        if not row:
            return jsonify(Error = "Reservation Not Found"), 404
        else:
            reservation = self.fixDict(row)
            return jsonify(Reservation = reservation)

    def getReservationsByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer not found."), 404
        else:
            reservation_list = []
            dao = ReservationDAO()
            reservation_list = dao.getReservationsByCustomerId(customer_id)
            result_list = self.fixDict(reservation_list)
            return jsonify(Reservations = result_list)

    def getResourcesByReservationId(self, reservation_id):
        reservation_dao = ReservationDAO()
        if not reservation_dao.getReservationById(reservation_id):
            return jsonify(Error = "Reservation Not Found"), 404
        else:
            resources_list = []
            result_list = []
            resources_list = reservation_dao.getResourcesByReservationId(reservation_id)
            for row in resources_list:
                result = ResourceHandler().build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources = result_list)

    def searchReservations(self, args):
        reservation_date = args.get("reservation_date")
        reservation_status = args.get("reservation_status")
        dao = ReservationDAO()
        reservation_list = []
        if (len(args) == 1) and reservation_date:
            reservation_list = dao.getReservationsByDate(reservation_date)
        elif (len(args) == 1) and reservation_status:
            reservation_list = dao.getReservationsByStatus(reservation_status)
        elif (len(args) == 2) and reservation_date and reservation_status:
            reservation_list = dao.getReservationsByDateAndStatus(reservation_date, reservation_status)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = self.fixDict(reservation_list)
        return jsonify(Reservations = result_list)

    def insertReservation(self, json):
        customer_id = json["customer_id"]
        request_id = json["request_id"]
        reservation_date = json["reservation_date"]
        reservation_status = json["reservation_status"]
        resources = json["resources"]

        if customer_id and reservation_date and reservation_status and resources:
            reservation_dao = ReservationDAO()
            resourceReservation_dao = ResourceReservationDAO()
            reservation_id = reservation_dao.insert(customer_id, request_id, reservation_date, reservation_status)

            for resource in resources:
                resourceReservation_dao.insert(reservation_id, resource["resource_id"], resource["reservation_quantity"])

            if request_id:
                request_dao = RequestDAO()
                request = request_dao.getRequestById(request_id)
                request_dao.update(request_id, request[0][1], request[0][2], request[0][3], request[0][4], "Accepted")

            result = self.build_reservation_attributes(reservation_id, customer_id, request_id, reservation_date, reservation_status, resources)
            return jsonify(Reservation = result), 201

        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateReservation(self, reservation_id, json):
        reservation_dao = ReservationDAO()
        resourceReservation_dao = ResourceReservationDAO()
        if not reservation_dao.getReservationById(reservation_id):
            return jsonify(Error = "Reservation not found."), 404
        else:
            customer_id = json["customer_id"]
            request_id = json["request_id"]
            reservation_date = json["reservation_date"]
            reservation_status = json["reservation_status"]
            resources = json["resources"]

            if customer_id and reservation_date and reservation_status and resources:
                reservation_dao = ReservationDAO()
                reservation_id = reservation_dao.update(reservation_id, customer_id, request_id, reservation_date, reservation_status)
                
                for resource in resources:
                    resourceReservation_dao.update(reservation_id, resource["resource_id"], resource["reservation_quantity"])
                
                result = self.build_reservation_attributes(reservation_id, customer_id, request_id, reservation_date, reservation_status, resources)
                return jsonify(Reservation = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in put request"), 400

    def deleteReservation(self, reservation_id):
        reservation_dao = ReservationDAO()
        resourceReservation_dao = ResourceReservationDAO()
        if not reservation_dao.getReservationById(reservation_id):
            return jsonify(Error = "Reservation not found."), 404
        else:
            resourceReservation_dao.delete(reservation_id)
            reservation_dao.delete(reservation_id)
            return jsonify(DeleteStatus = "OK"), 200