from config.dbconfig import pg_config
import psycopg2
class RequestDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # request = request_id, customer_id, request_title, request_date, request_description, request_status

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category natural inner join category order by request_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category natural inner join category where request_id = %s order by request_id;"
        cursor.execute(query, (request_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByCustomerId(self, customer_id):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category natural inner join category where customer_id = %s order by request_id;"
        cursor.execute(query, (customer_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByTitle(self, request_title):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category natural inner join category where request_title = %s order by request_id;"
        cursor.execute(query, (request_title,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByStatus(self, request_status):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category natural inner join category where request_status = %s order by request_id;"
        cursor.execute(query, (request_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByCategoryName(self, category_name):
        cursor = self.conn.cursor()
        query = "select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category natural inner join category where category_name = %s order by request_id;"
        cursor.execute(query, (category_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, customer_id, request_title, request_date, request_description, request_status):
        cursor = self.conn.cursor()
        query = "insert into request(customer_id, request_title, request_date, request_description, request_status) values (%s, %s, %s, %s, %s) returning request_id;"
        cursor.execute(query, (customer_id, request_title, request_date, request_description, request_status))
        request_id = cursor.fetchone()[0]
        self.conn.commit()
        return request_id

    def update(self, request_id, customer_id, request_title, request_date, request_description, request_status):
        cursor = self.conn.cursor()
        query = "update request set customer_id = %s, request_title = %s, request_date = %s, request_description = %s, request_status = %s where request_id = %s;"
        cursor.execute(query, (customer_id, request_title, request_date, request_description, request_status, request_id,))
        self.conn.commit()
        return request_id

    def delete(self, request_id):
        cursor = self.conn.cursor()
        query = "delete from request where request_id = %s;"
        cursor.execute(query,(request_id,))
        self.conn.commit()
        return request_id