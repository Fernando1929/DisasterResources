from config.dbconfig import pg_config
import psycopg2
class CreditCardDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # creditcard = creditcard_id, payment_id, customer_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date

    def getAllCreditCards(self):
        cursor = self.conn.cursor()
        query = "select * from creditcard natural inner join payment;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardById(self, creditcard_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard natural inner join payment where creditcard_id = %s;"
        cursor.execute(query, (creditcard_id,))
        result = cursor.fetchone()
        return result

    def getCreditCardByName(self, creditcard_name):
        cursor = self.conn.cursor()
        query = "select * from creditcard natural inner join payment where creditcard_name = %s;"
        cursor.execute(query, (creditcard_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardByNumber(self, creditcard_number):
        cursor = self.conn.cursor()
        query = "select * from creditcard natural inner join payment where creditcard_number = %s;"
        cursor.execute(query, (creditcard_number,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardByCustomerId(self, customer_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard natural inner join payment where customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result

    def insert(self, payment_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date):
        cursor = self.conn.cursor()
        query = "insert into creditcard(payment_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date) values (%s, %s, %s, %s, %s) returning creditcard_id;"
        cursor.execute(query, (payment_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date))
        creditcard_id = cursor.fetchone()[0]
        self.conn.commit()
        return creditcard_id

    def update(self, creditcard_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date):
        payment_id = 1
        return payment_id

    def delete(self, creditcard_id):
        payment_id = 1
        return payment_id