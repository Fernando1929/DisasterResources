from flask import jsonify
from dao.reservation import ReservationDAO
from dao.user import UserDAO

class ReservationHandler:

    def build_reservation_dict(self, row):
        result = {}
        result['reservation_id'] = row[0]
        result['customer_id'] = row[1]
        result['reservation_date'] = row[2]
        result['reservation_quantity'] = row[3]
        result['reservation_status'] = row[4]
        return result

    def build_reservation_attributes(self, reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status):
        result = {}
        result['reservation_id'] = reservation_id
        result['customer_id'] = customer_id
        result['reservation_date'] = reservation_date
        result['reservation_quantity'] = reservation_quantity
        result['reservation_status'] = reservation_status
        return result

    def getAllReservations(self):
        dao = ReservationDAO()
        reservation_list = dao.getAllReservations()
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservations = result_list)

    def getReservationById(self, reservation_id):
        dao = ReservationDAO()
        row = dao.getReservationById(reservation_id)
        if not row:
            return jsonify(Error = "Reservation Not Found"), 404
        else:
            reservation = self.build_reservation_dict(row)
            return jsonify(Reservation = reservation)

    def getReservationsByCustomerId(self, customer_id):
        # user_dao = UserDAO()
        # if not user_dao.getUserById(customer_id):
        #     return jsonify(Error = "User not found."), 404
        # else:
        reservation_list = []
        result_list = []
        dao = ReservationDAO()
        reservation_list = dao.getReservationsByCustomerId(customer_id)
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservations = result_list)

    def searchReservation(self, args):
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
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation = result_list)

    def insertReservation(self, json):
        customer_id = json["customer_id"]
        reservation_date = json["reservation_date"]
        reservation_quantity = json["reservation_quantity"]
        reservation_status = json["reservation_status"]

        if customer_id and reservation_date and reservation_quantity and reservation_status:
            reservation_dao = ReservationDAO()
            reservation_id = reservation_dao.insert(customer_id, reservation_date, reservation_quantity, reservation_status)
            result = self.build_reservation_attributes(reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status)
            return jsonify(Reservation = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateReservation(self, reservation_id, json):
        reservation_dao = ReservationDAO()
        if not reservation_dao.getReservationById(reservation_id):
            return jsonify(Error = "Reservation not found."), 404
        else:
            customer_id = json["customer_id"]
            reservation_date = json["reservation_date"]
            reservation_quantity = json["reservation_quantity"]
            reservation_status = json["reservation_status"]

            if customer_id and reservation_date and reservation_quantity and reservation_status:
                reservation_dao = ReservationDAO()
                reservation_id = reservation_dao.insert(customer_id, reservation_date, reservation_quantity, reservation_status)
                result = self.build_reservation_attributes(reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status)
                return jsonify(Reservation = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteReservation(self, reservation_id):
        reservation_dao = ReservationDAO()
        if not reservation_dao.getReservationById(reservation_id):
            return jsonify(Error = "Reservation not found."), 404
        else:
            reservation_dao.delete(reservation_id)
            return jsonify(DeleteStatus = "OK"), 200