from flask import Flask, jsonify, request
from handler.ice import IceHandler
from handler.supplier import SupplierHandler
from handler.admin import AdminHandler
from handler.order import OrderHandler
from handler.generator import GeneratorHandler
from handler.battery import BatteryHandler

#from handler.supplier import SupplierHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the Disaster Resources Locator App!'

#################### Supplier Routes ####################

@app.route('/DRL/supplier', methods = ['GET','POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.json)
    else :
        if not request.args:
            return SupplierHandler().getAllSupplier()
        else:
            return SupplierHandler().searchSupplier(request.args)

@app.route('/DRL/supplier/<int:supplier_id>', methods = ['GET','PUT','DELETE'])
def getSupplierById(supplier_id):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(supplier_id)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(supplier_id, request.json)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(supplier_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/supplier/<int:supplier_id>/resources', methods=['GET','POST']) 
def getAllSupplierResources(supplier_id):
    if request.method == 'POST':
        #adds resource 
        pass
    else:
        if not request.args:
            return SupplierHandler().getAllSupplierResources(supplier_id)
        else:
            return SupplierHandler().searchSupplier(request.args)

@app.route('/DRL/supplier/<int:supplier_id>/resources/<int:order_id>',methods=['GET', 'PUT','DELETE'])
def getSupplierResourcesById(supplier_id, order_id):
    if request.method == 'GET':
        return SupplierHandler().getSupplierResourceById(supplier_id,order_id)
    elif request.method == 'PUT':
        #return SupplierHandler().updateSupplierResource(supplier_id, request.json)
        pass
    elif request.method == 'DELETE':
        #return SupplierHandler().deleteSupplierResource(supplier_id)
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

#################### Admin Routes ####################

@app.route('/DRL/admin', methods = ['GET','POST'])
def getAllAdmin():
    if request.method == 'POST':
        return AdminHandler().insertAdmin(request.json)
    else :
        if not request.args:
            return AdminHandler().getAllAdmin()
        else:
            return AdminHandler().searchAdmin(request.args)

@app.route('/DRL/admin/<int:admin_id>', methods = ['GET','PUT','DELETE'])
def getAdminById(admin_id):
    if request.method == 'GET':
        return AdminHandler().getAdminById(admin_id)
    elif request.method == 'PUT':
        return AdminHandler().updateAdmin(admin_id,request.json)
    elif request.method == 'DELETE':
        return AdminHandler().deleteAdmin(admin_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

#################### Battery Routes ####################

@app.route('/DRL/customer/<int:customer_id>/order', methods=['GET','POST'])
def getAllOrder(customer_id):
    if request.method == 'POST':
        return OrderHandler().insertOrder(request.json)
    else:
        if not request.args:
            return OrderHandler().getAllOrders(customer_id)
        else:
            return OrderHandler().searchOrders(request.args)

@app.route('/DRL/customer/<int:customer_id>/order/<int:order_id>', methods=['GET', 'PUT','DELETE'])
def getOrderById(customer_id, order_id):
    if request.method == 'GET':
        return OrderHandler().getCustomerOrderById(customer_id, order_id)
    elif request.method == 'PUT':
        return OrderHandler().updateOrder(order_id, request.json)
    elif request.method == 'DELETE':
        return OrderHandler().deleteOrder(order_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

#################### Ice Routes ####################

@app.route('/DRL/resources/ice', methods = ['GET','POST'])
def getAllIce():
    if request.method == 'POST':
        return IceHandler().insertIce(request.json)
    else :
        if not request.args:
            return IceHandler().getAllIce()
        else:
            return IceHandler().searchIce(request.args)

@app.route('/DRL/resources/ice/<int:ice_id>', methods = ['GET','PUT','DELETE'])
def getIceById(ice_id):
    if request.method == 'GET':
        return IceHandler().getIceById(ice_id)
    elif request.method == 'PUT':
        return IceHandler().updateIce(ice_id, request.json)
    elif request.method == 'DELETE':
        return IceHandler().deleteIce(ice_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

#################### Battery Routes ####################

@app.route('/DRL/resources/battery', methods = ['GET','POST'])
def getAllBattery():
    if request.method == 'POST':
        return BatteryHandler().insertBattery(request.json)
    else :
        if not request.args:
            return BatteryHandler().getAllBattery()
        else:
            return BatteryHandler().searchBattery(request.args)

@app.route('/DRL/resources/battery/<int:battery_id>', methods = ['GET','PUT','DELETE']) 
def getBatteryById(battery_id):
    if request.method == 'GET':
        return BatteryHandler().getBatteryById(battery_id)
    elif request.method == 'PUT':
        return BatteryHandler().updateBattery(battery_id, request.json)
    elif request.method == 'DELETE':
        return BatteryHandler().deleteBaterry(battery_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

#################### Generator Routes ####################

@app.route('/DRL/resources/generator',methods = ['GET','POST'])
def getAllGenerator():
    if request.method == 'POST':
        return GeneratorHandler().insertGenerator(request.json)
    else :
        if not request.args:
            return GeneratorHandler().getAllGenerator()
        else:
            return GeneratorHandler().searchGenerator(request.args)

@app.route('/DRL/resources/generator/<int:generator_id>', methods = ['GET','PUT','DELETE'])
def getGeneratorById(generator_id):
    if request.method == 'GET':
        return GeneratorHandler().getGeneratorById(generator_id)
    elif request.method == 'PUT':
        return GeneratorHandler().updateGenerator(generator_id, request.json)
    elif request.method == 'DELETE':
        return GeneratorHandler().deleteGenerator(generator_id)
    else:
        return jsonify(Error = "Method not allowed"), 405


if __name__ == '__main__':
    app.run(debug=True)

