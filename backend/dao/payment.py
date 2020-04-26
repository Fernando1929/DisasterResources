from config.dbconfig import pg_config
import psycopg2
class PaymentDAO:
    def _init_(self):
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
        return payment_id

    def delete(self, payment_id):
        return payment_id