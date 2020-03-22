from config.dbconfig import pg_config
import psycopg2

#Example
class OrderDAO:
    
    def __init__(self):
        super().__init__()

    #order = customer_id, payment_id, order_id, order_date, order_quantity, order_totalprice, order_status
    def getAllOrders(self):
        result = [
            ['1','2','1', '12/3/20', '3', '$30', 'pending'],
            ['1','2','2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def getOrderById(self, order_id):
        result = ['1','2','1', '12/3/20', '3', '$30', 'pending']
        return result

    def getOrderByCustomerId(self, customer_id):
        result = ['1','2','1', '12/3/20', '3', '$30', 'pending']
        return result

    def getOrdersByDate(self, order_date):
        result = [
           ['1','2','2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def getOrdersByStatus(self, order_status):
        result = [
            ['1','2','1', '12/3/20', '3', '$30', 'pending'],
            ['1','2','2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def getOrdersByDateAndStatus(self, order_date, order_status):
        result = [
            ['1','2','2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def insert(self, customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status):
        resource_id =1
        return resource_id

    def update(self, order_id, customer_id, payment_id, order_date, order_quantity, order_totalprice, order_status):
        resource_id =1
        return resource_id

    def delete(self, order_id):
        resource_id =1
        return resource_id