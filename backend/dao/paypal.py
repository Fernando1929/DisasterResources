from config.dbconfig import pg_config
import psycopg2
class PaypalDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPaypal(self):
        cursor = self.conn.cursor()
        query = "select * from paypal natural inner join payment;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPaypalById(self, paypal_id):
        cursor = self.conn.cursor()
        query = "select * from paypal natural inner join payment where paypal_id = %s;"
        cursor.execute(query, (paypal_id,))
        result = cursor.fetchone()
        return result

    def getPaypalByPaymentId(self, payment_id):
        cursor = self.conn.cursor()
        query = "select * from paypal natural inner join payment where payment_id = %s;"
        cursor.execute(query, (payment_id,))
        result = cursor.fetchone()
        return result

    def getPaypalByUsername(self, paypal_username):
        cursor = self.conn.cursor()
        query = "select * from paypal natural inner join payment where paypal_username = %s;"
        cursor.execute(query, (paypal_username,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPaypalByPassword(self, paypal_password):
        cursor = self.conn.cursor()
        query = "select * from paypal natural inner join payment where paypal_password = %s;"
        cursor.execute(query, (paypal_password,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPaypalByCustomerId(self, customer_id):
        cursor = self.conn.cursor()
        query = "select * from paypal natural inner join payment where customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result

    def insert(self, payment_id, paypal_username, paypal_password):
        cursor = self.conn.cursor()
        query = "insert into paypal(payment_id, paypal_username, paypal_password) values (%s, %s, %s) returning paypal_id;"
        cursor.execute(query, (payment_id, paypal_username, paypal_password))
        paypal_id = cursor.fetchone()[0]
        self.conn.commit()
        return paypal_id

    def update(self, paypal_id, paypal_username, paypal_password):
        payment_id = 1
        return payment_id

    def delete(self, paypal_id):
        payment_id = 1
        return payment_id