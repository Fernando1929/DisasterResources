from config.dbconfig import pg_config
import psycopg2
class CustomerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # customer = customer_id, user_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone

    def getAllCustomers(self):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomerById(self, customer_id):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result

    def getCustomersByFirstname(self, customer_firstname):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where user_firstname = %s;"
        cursor.execute(query, (customer_firstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomersByLastname(self, customer_lastname):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where user_lastname = %s;"
        cursor.execute(query, (customer_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomersByFirstnameAndLastname(self, customer_firstname, customer_lastname):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where user_firstname = %s and user_lastname = %s;"
        cursor.execute(query, (customer_firstname, customer_lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomerByEmail(self, customer_email):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where user_email = %s;"
        cursor.execute(query, (customer_email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomerByPhone(self, customer_phone):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where user_phone = %s;"
        cursor.execute(query, (customer_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCustomersByDateOfBirth(self, customer_date_birth):
        cursor = self.conn.cursor()
        query = "select * from customer natural inner join users natural inner join user_phone where user_date_birth = %s;"
        cursor.execute(query, (customer_date_birth,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, user_id):
        cursor = self.conn.cursor()
        query = "insert into customer(user_id) values (%s) returning customer_id;"
        cursor.execute(query, (user_id,))
        customer_id = cursor.fetchone()[0]
        self.conn.commit()
        return customer_id

    def update(self, customer_id):
        user_id = 1
        return user_id

    def delete(self, customer_id):
        user_id = 1
        return user_id