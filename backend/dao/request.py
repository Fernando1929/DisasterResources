from config.dbconfig import pg_config
import psycopg2
class RequestDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # request = request_id, customer_id, request_title, resource_category, request_date, request_description, request_quantity, request_status

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getRequestsByCustomerId(self, customer_id):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join category where customer_id = %s;"
        cursor.execute(query, (customer_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByTitle(self, request_title):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join category where request_title = %s;"
        cursor.execute(query, (request_title,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByStatus(self, request_status):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join category where request_status = %s;"
        cursor.execute(query, (request_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, customer_id, request_title, request_date, request_status, request_description):
        cursor = self.conn.cursor()
        query = "insert into request(customer_id, request_title, request_date, request_status, request_description) values (%s, %s, %s, %s, %s) returning request_id;"
        cursor.execute(query, (customer_id, request_title, request_date, request_status))
        request_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_id

    def update(self, request_id, customer_id, request_title, request_date, request_status, request_description):
        return request_id

    def delete(self, request_id):
        return request_id