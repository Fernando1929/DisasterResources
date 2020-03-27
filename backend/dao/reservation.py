# from config.dbconfig import pg_config
# import psycopg2

class ReservationDAO:
    
    def __init__(self):
        super().__init__()

    #reservation = reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status

    def getAllReservations(self):
        result = [[1,1, '12/31/2020', 10, 'Accepted']]
        return result

    def getReservationById(self, reservation_id):
        result = [1,1, '12/31/2020', 10, 'Accepted']
        return result

    def getReservationsByDate(self, reservation_date):
        result = [[1,1, '12/31/2020', 10, 'Accepted']]
        return result

    def getReservationsByStatus(self, reservation_status):
        result = [[1,1, '12/31/2020', 10, 'Accepted']]
        return result

    def getReservationsByDateAndStatus(self, reservation_date, reservation_status):
        result = [[1,1, '12/31/2020', 10, 'Accepted']]
        return result

    def getReservationsByCustomerId(self, customer_id):
        result = [[1,1, '12/31/2020', 10, 'Accepted']]
        return result

    def insert(self, customer_id, reservation_date, reservation_quantity, reservation_status):
        reservation_id = 1
        return reservation_id

    def update(self, reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status):
        return reservation_id

    def delete(self, reservation_id):
        return reservation_id