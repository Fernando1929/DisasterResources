from flask import jsonify
from dao.order import OrderDAO
from dao.customer import CustomerDAO
from dao.resourceOrders import ResourceOrdersDAO
from handler.athMovil import AthMovilHandler
from handler.creditCard import CreditCardHandler
from handler.paypal import PaypalHandler

class OrderHandler:

    def build_order_dict(self, row, resources):
        result = {}
        result['order_id'] = row[0]
        result['customer_id'] = row[1]
        result['payment_id'] = row[2]
        result['request_id'] = row[3]
        result['order_date'] = row[4]
        result['order_price'] = row[5]
        result['order_status'] = row[6]
        result['resources'] =  resources
        return result

    def build_order_attributes(self, order_id, customer_id, payment_id, request_id, order_date, order_price, order_status, resources):
        result = {}
        result['customer_id'] = customer_id
        result['payment_id'] = payment_id
        result['request_id'] = request_id
        result['order_id'] = order_id 
        result['order_date'] = order_date
        result['order_price'] = order_price
        result['order_status'] = order_status
        result['resources'] = resources
        return result
    
    def build_resources_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['resource_name'] = row[1]
        result['order_quantity'] = row[2]
        result['discount'] = row[3]
        return result

    def fixDict(self, request_list):
        result_list = []
        resources_list = []
        index = 1
        for row in request_list:
            if index < len(request_list) and row[0] == request_list[index][0]:
                resources_list.append(row[6:])
            else:
                resources_list.append(row[6:])
                result = self.build_order_dict(row[:6], self.createResourceDict(resources_list))
                result_list.append(result)
                resources_list.clear()
            index += 1
        return result_list

    def createResourceDict(self, resources_list):
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return result_list

    def getAllOrders(self):
        dao = OrderDAO()
        result = dao.getAllOrders()
        result_list = self.fixDict(result)
        return jsonify(Orders = result_list)

    def getOrderById(self, order_id):
        dao = OrderDAO()
        row = dao.getOrderById(order_id)
        if not row:
            return jsonify(Error = "Order Not Found"), 404
        else:
            order = self.fixDict(row)
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
        result_list = self.fixDict(orders_list)
        return jsonify(Orders = result_list)

    def getOrderByCustomerId(self, customer_id):
        customer_dao = CustomerDAO()
        if not customer_dao.getCustomerById(customer_id):
            return jsonify(Error = "Customer Not Found"), 404
        else:
            orders_list = []
            dao = OrderDAO()
            orders_list = dao.getOrderByCustomerId(customer_id)
            result_list = self.fixDict(orders_list)
            return jsonify(Orders = result_list)

    def getPaymentByOrderId(self, order_id):
        dao = OrderDAO()
        row = dao.getOrderById(order_id)
        if not row:
            return jsonify(Error = "Order Not Found"), 404
        else:
            result = self.fixDict(row)
            payment_id = result[0]["payment_id"]
            ath_movil = AthMovilHandler().getAthMovilByPaymentId(payment_id)
            creditcard = CreditCardHandler().getCreditCardByPaymentId(payment_id)
            paypal = PaypalHandler().getPaypalByPaymentId(payment_id)
            
            if ath_movil: 
                return ath_movil
            elif creditcard:
                return creditcard
            elif paypal:
                return paypal
            else:
                return jsonify(Error = "Payment Not Found"), 404

    def getResourcesByOrderId(self, order_id):
        dao = OrderDAO()
        row = dao.getOrderById(order_id)
        if not row:
            return jsonify(Error = "Order Not Found"), 404
        else:
            result = self.fixDict(row)
            resource_list = result[0]["resources"]
            return jsonify(Resources = resource_list)

    def insertOrder(self, json):
        customer_id = json['customer_id']
        payment_id = json['payment_id']
        request_id = json['request_id']
        order_date = json['order_date'] 
        order_price = json['order_price'] 
        order_status = json['order_status']
        resources =  json['resources']

        if customer_id and payment_id and order_date and order_price and order_status and resources:
            order_dao = OrderDAO()
            resourceOrders_dao = ResourceOrdersDAO()
            order_id = order_dao.insert(customer_id, payment_id, request_id, order_date, order_price, order_status)

            for resource in resources:
                resourceOrders_dao.insert(order_id, resource["resource_id"], resource["order_quantity"], resource["discount"])

            result = self.build_order_attributes(order_id, customer_id, payment_id, request_id, order_date, order_price, order_status, resources)
            return jsonify(Order = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteOrder(self, order_id):
        order_dao = OrderDAO()
        resourceOrders_dao =  ResourceOrdersDAO()
        if not order_dao.getOrderById(order_id):
            return jsonify(Error = "Order not found."), 404
        else:
            resourceOrders_dao.delete(order_id)
            order_dao.delete(order_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateOrder(self, order_id, json):
        order_dao = OrderDAO()
        resourceOrders_dao =  ResourceOrdersDAO()
        if not order_dao.getOrderById(order_id):
            return jsonify(Error = "Order not found."), 404
        else:
            customer_id = json['customer_id']
            payment_id = json['payment_id']
            request_id = json['request_id']
            order_date = json['order_date']
            order_price = json['order_price']
            order_status = json['order_status']
            resources = json['resources']

            if customer_id and payment_id and order_date and order_price and order_status and resources:
                order_dao.update(order_id, customer_id, payment_id, request_id, order_date, order_price, order_status)

                for resource in resources:
                    resourceOrders_dao.update(order_id, resource["resource_id"], resource["order_quantity"], resource["discount"])

                result = self.build_order_attributes(order_id, customer_id, payment_id, request_id, order_date, order_price, order_status, resources)
                return jsonify(Order = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400
