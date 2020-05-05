from config.dbconfig import pg_config
import psycopg2

class OrderDAO:

    #order = customer_id, payment_id, order_id, order_date, order_quantity, order_price, order_status
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self): #Fix tomorrow put every param in order for the dict
        cursor = self.conn.cursor() #select request_id, customer_id, request_title, request_date, request_description, request_status, category_id, category_name, request_quantity from request natural inner join request_category"
        query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource;" #Maybe añadir el Join de con category a ver discutirlo mañana
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, order_id):
        cursor = self.conn.cursor()
        query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource where order_id = %s;"
        cursor.execute(query,(order_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByCustomerId(self, customer_id):#maybe change methods name to ordersBy customer Id 
        cursor = self.conn.cursor()
        query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource where customer_id = %s;"
        cursor.execute(query,(customer_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getOrderByPaymentId(self, payment_id):
    #     cursor = self.conn.cursor()
    #     query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource where payment_id = %s;"
    #     cursor.execute(query,(payment_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getOrdersByDate(self, order_date):
        cursor = self.conn.cursor()
        query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource where order_date = %s;"
        cursor.execute(query,(order_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByStatus(self, order_status):
        cursor = self.conn.cursor()
        query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource where order_status = %s;"
        cursor.execute(query,(order_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByDateAndStatus(self, order_date, order_status):
        cursor = self.conn.cursor()
        query = "select order_id, customer_id, payment_id, order_date, order_price, order_status, resource_id, resource_name, order_quantity, discount from orders natural inner join resource_orders natural inner join resource where order_date = %s and order_status = %s;"
        cursor.execute(query,(order_date, order_status))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, customer_id, payment_id, order_date, order_price, order_status):
        cursor = self.conn.cursor()
        query = "insert into orders(customer_id, payment_id, order_date, order_price, order_status) values(%s,%s,%s,%s,%s) returning order_id;"
        cursor.execute(query,(customer_id, payment_id, order_date, order_price, order_status))
        order_id = cursor.fetchone()[0]
        self.conn.commit()
        return order_id

    def update(self, order_id, customer_id, payment_id, order_date, order_price, order_status):
        cursor = self.conn.cursor()
        query = "update orders set customer_id = %s, payment_id = %s, order_date = %s, order_price = %s, order_status = %s where order_id = %s"
        cursor.execute(query,(customer_id, payment_id, order_date, order_price, order_status, order_id))
        self.conn.commit()
        return order_id

    def delete(self, order_id):
        cursor = self.conn.cursor()
        query = "delete from orders where order_id = %s;"
        cursor.execute(query,(order_id,))
        self.conn.commit()
        return order_id