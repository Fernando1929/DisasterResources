from config.dbconfig import pg_config
import psycopg2
class PaymentDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, customer_id):
        cursor = self.conn.cursor()
        query = "insert into payment(customer_id) values (%s) returning payment_id;"
        cursor.execute(query, (customer_id,))
        payment_id = cursor.fetchone()[0]
        self.conn.commit()
        return payment_id

    def update(self, payment_id, user_id):
        cursor = self.conn.cursor()
        query = "update payment set user_id = %s where payment_id = %s returning payment_id;"
        cursor.execute(query, (user_id, payment_id))
        payment_id = cursor.fetchone()[0]
        self.conn.commit()
        return payment_id
    
    def delete(self, payment_id):
        cursor = self.conn.cursor()
        query = "delete from payment where payment_id = %s returning payment_id;"
        cursor.execute(query,(payment_id,))
        payment_id = cursor.fetchone()[0]
        self.conn.commit()
        return payment_id