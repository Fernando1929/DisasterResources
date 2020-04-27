from config.dbconfig import pg_config
import psycopg2

class OrderDAO:

    #order = customer_id, payment_id, order_id, order_date, order_quantity, order_totalprice, order_status
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "Select * from order;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, order_id):
        cursor = self.conn.cursor()
        query = "Select * from order where order_id = %s;"
        cursor.execute(query,(order_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByCustomerId(self, customer_id):#maybe change methods name to ordersBy customer Id 
        cursor = self.conn.cursor()
        query = "Select * from order where customer_id = %s;"
        cursor.execute(query,(customer_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByDate(self, order_date):
        cursor = self.conn.cursor()
        query = "Select * from order where order_date = %s;"
        cursor.execute(query,(order_date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByStatus(self, order_status):
        cursor = self.conn.cursor()
        query = "Select * from order where order_status = %s;"
        cursor.execute(query,(order_status))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByDateAndStatus(self, order_date, order_status):
        cursor = self.conn.cursor()
        query = "Select * from order where order_date = %s and order_status = %s;"
        cursor.execute(query,(order_date, order_status))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status):
        cursor = self.conn.cursor()
        query = "insert into order(customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status) values(%s,%s,%s,%s,%s,%s) returning order_id;"
        cursor.execute(query,(customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status))
        order_id = cursor.fetchone()[0]
        self.conn.commit()
        return order_id

    def update(self, order_id, customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status):
        cursor = self.conn.cursor()
        query = "update company set company_name = %s, company_address = %s, company_phone = %s where order_id = %s;"
        cursor.execute(query,(customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status, order_id))
        self.conn.commit()
        return order_id

    def delete(self, order_id):
        cursor = self.conn.cursor()
        query = "delete from order where order_id = %s;"
        cursor.execute(query,(order_id))
        self.conn.commit()
        return order_id