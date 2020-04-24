from config.dbconfig import pg_config
import psycopg2

class ReservationDAO:
    
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    #reservation = reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status

    def getAllReservations(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, reservation_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation WHERE reservation_id = %s;"
        cursor.execute(query, (reservation_id,))
        result = cursor.fetchone()
        return result

    def getReservationsByDate(self, reservation_date):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation WHERE reservation_date = %s;"
        cursor.execute(query, (reservation_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationsByStatus(self, reservation_status):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation WHERE reservation_status = %s;"
        cursor.execute(query, (reservation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationsByDateAndStatus(self, reservation_date, reservation_status):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation WHERE reservation_date = %s AND reservation_status = %s;"
        cursor.execute(query, (reservation_date, reservation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationsByCustomerId(self, customer_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation WHERE customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, customer_id, reservation_date, reservation_quantity, reservation_status):
        cursor = self.conn.cursor()
        query = "INSERT INTO reservation (customer_id, reservation_date, reservation_quantity, reservation_status) VALUES (%s, %s, %s, %s) RETURNING reservation_id;"
        cursor.execute(query, (customer_id, reservation_date, reservation_quantity, reservation_status,))
        reservation_id = cursor.fetchone()[0]
        self.conn.commit()
        return reservation_id

    def update(self, reservation_id, customer_id, reservation_date, reservation_quantity, reservation_status):
        return reservation_id

    def delete(self, reservation_id):
        return reservation_id