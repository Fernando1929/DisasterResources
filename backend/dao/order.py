from config.dbconfig import pg_config
import psycopg2

#Example
class OrderDAO:
    
    def __init__(self):
        super().__init__()

    #order = order_id, order_date, order_cuantity, order_totalprice, order_status
    def getAllOrders(self):
        result = [
            ['1', '12/3/20', '3', '$30', 'pending'],
            ['2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def getOrderById(self, pid):
        result = [
            ['1', '12/3/20', '3', '$30', 'pending']
        ]
        return result

    def getCustomerOrderById(self, customer_id, order_id):
        result = ['1', '12/3/20', '3', '$30', 'pending']
        return result

    def getOrdersByDate(self, order_date):
        result = [
            ['2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def getOrdersByStatus(self, order_status):
        result = [
            ['1', '12/3/20', '3', '$30', 'pending'],
            ['2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def getOrdersByDateAndStatus(self, order_date, order_status):
        result = [
            ['2', '4/3/20', '10', '$100', 'delivered']
        ]
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        resource_id =1
        return resource_id

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        resource_id =1
        return resource_id

    def delete(self, pid):
        resource_id =1
        return resource_id