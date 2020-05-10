from config.dbconfig import pg_config
import psycopg2
class AthMovilDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ath movil = ath_movil_id, payment_id, customer_id, ath_movil_phone

    def getAllAthMovil(self):
        cursor = self.conn.cursor()
        query = "select * from ath_movil natural inner join payment;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAthMovilById(self, ath_movil_id):
        cursor = self.conn.cursor()
        query = "select * from ath_movil natural inner join payment where ath_movil_id = %s;"
        cursor.execute(query, (ath_movil_id,))
        result = cursor.fetchone()
        return result

    def getAthMovilByPaymentId(self, payment_id):
        cursor = self.conn.cursor()
        query = "select * from ath_movil natural inner join payment where payment_id = %s;"
        cursor.execute(query, (payment_id,))
        result = cursor.fetchone()
        return result

    def getAthMovilByPhone(self, ath_movil_phone):
        cursor = self.conn.cursor()
        query = "select * from ath_movil natural inner join payment where ath_movil_phone = %s;"
        cursor.execute(query, (ath_movil_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAthMovilByCustomerId(self, customer_id):
        cursor = self.conn.cursor()
        query = "select * from ath_movil natural inner join payment where customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result

    def insert(self, payment_id, ath_movil_phone):
        cursor = self.conn.cursor()
        query = "insert into ath_movil(payment_id, ath_movil_phone) values (%s, %s) returning ath_movil_id;"
        cursor.execute(query, (payment_id, ath_movil_phone))
        ath_movil_id = cursor.fetchone()[0]
        self.conn.commit()
        return ath_movil_id

    def update(self, ath_movil_id, ath_movil_phone):
        payment_id = 1
        return payment_id

    def delete(self, ath_movil_id):
        payment_id = 1
        return payment_id