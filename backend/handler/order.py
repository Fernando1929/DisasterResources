from flask import jsonify
from dao.order import OrderDAO

class OrderHandler:

    #order = order_id, order_date, order_cuantity, order_totalprice, order_status
    def build_order_dict(self, row):
        result = {}
        result['order_id'] = row[0]
        result['order_date'] = row[1]
        result['order_cuantity'] = row[2]
        result['order_totalprice'] = row[3]
        result['order_status'] = row[4]
        return result

    def build_order_attributes(self, order_id, order_date, order_cuantity, order_totalprice, order_status):
        result = {}
        result['order_id'] = order_id 
        result['order_date'] = order_date
        result['order_totalprice'] = order_cuantity 
        result['order_cuantity'] = order_totalprice
        result['order_status'] = order_status
        return result

    def getAllOrders(self, customer_id):
        dao = OrderDAO()
        result = dao.getAllOrders()
        result_list = []
        for row in result:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getOrderById(self, order_id):
        dao = OrderDAO()
        row = dao.getOrderById(order_id)
        if not row:
            return jsonify(Error = "Order Not Found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order = order)

    def searchOrders(self, args):
        order_date = args.get("order_date")
        order_status = args.get("order_status")
        dao = OrderDAO()
        orders_list = []
        if (len(args) == 2) and order_date and order_status:
            orders_list = dao.getOrdersByDateAndStatus(order_date, order_status)
        elif (len(args) == 1) and order_date:
            orders_list = dao.getOrdersByDate(order_date)
        elif (len(args) == 1) and order_status:
            orders_list = dao.getOrdersByStatus(order_status)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getCustomerOrderById(self, customer_id,order_id):
        dao = OrderDAO()
        row = dao.getCustomerOrderById(customer_id, order_id)
        if not row:
            return jsonify(Error = "Order Not Found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order = order)

    def insertOrder(self, json):
        order_date = json['order_date'] 
        order_cuantity = json['order_totalprice'] 
        order_totalprice = json['order_cuantity'] 
        order_status = json['order_status']
        if order_date and order_cuantity and order_totalprice and order_status:
            dao = OrderDAO()
            order_id = dao.insert(order_date, order_cuantity, order_totalprice, order_status)
            json = self.build_order_attributes(order_id, order_date, order_cuantity, order_totalprice, order_status) #change parameters
            return jsonify(Order=json), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteOrder(self, order_id):
        dao = OrderDAO()
        if not dao.getOrderById(order_id):
            return jsonify(Error = "Order not found."), 404
        else:
            dao.delete(order_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateOrder(self, order_id, json):
        dao = OrderDAO()
        if not dao.getOrderById(order_id):
            return jsonify(Error = "Order not found."), 404
        else:
            order_id = json['order_id']
            order_date = json['order_date']
            order_cuantity = json['order_cuantity']
            order_totalprice = json['order_totalprice']
            order_status = json['order_status']
            
            if order_id and order_date and order_cuantity and order_totalprice and order_status:
                dao.update(order_id, order_date, order_cuantity, order_totalprice, order_status)
                result = self.build_order_attributes(order_id, order_date, order_cuantity, order_totalprice, order_status)
                return jsonify(Order=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400
