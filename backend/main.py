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

@app.route('/DRL/supplier/<int:supplier_id>/resources', methods=['GET']) 
def getAllResourcesBySupplierId(supplier_id):
    return SupplierHandler().getAllSupplierResources(supplier_id)
       
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

#################### Order Routes ####################

@app.route('/DRL/customer/order', methods=['GET','POST'])
def getAllOrder():
    if request.method == 'POST':
        return OrderHandler().insertOrder(request.json)
    else:
        if not request.args:
            return OrderHandler().getAllOrders()
        else:
            return OrderHandler().searchOrders(request.args)

@app.route('/DRL/customer/order/<int:order_id>', methods=['GET', 'PUT','DELETE']) #modify
def getOrderById(order_id):
    if request.method == 'GET':
        return OrderHandler().getOrderById(order_id)
    elif request.method == 'PUT':
        return OrderHandler().updateOrder(order_id, request.json)
    elif request.method == 'DELETE':
        return OrderHandler().deleteOrder(order_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/customer/<int:customer_id>/order', methods=['GET'])
def getOrderByCustomerId(customer_id):
    return OrderHandler().getOrderByCustomerId(customer_id)

#################### Ice Routes ####################

@app.route('/DRL/ice', methods = ['GET','POST'])
def getAllIce():
    if request.method == 'POST':
        return IceHandler().insertIce(request.json)
    else :
        if not request.args:
            return IceHandler().getAllIce()
        else:
            return IceHandler().searchIce(request.args)

@app.route('/DRL/ice/<int:ice_id>', methods = ['GET','PUT','DELETE'])
def getIceById(ice_id):
    if request.method == 'GET':
        return IceHandler().getIceById(ice_id)
    elif request.method == 'PUT':
        return IceHandler().updateIce(ice_id, request.json)
    elif request.method == 'DELETE':
        return IceHandler().deleteIce(ice_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/ice/available', methods = ['GET'])
def getAllAvailableIce():
    return IceHandler().getAllAvailableIce()

@app.route('/DRL/ice/reserved', methods = ['GET'])
def getAllReservedIce():
    return IceHandler().getAllReservedIce()

#################### Battery Routes ####################

@app.route('/DRL/battery', methods = ['GET','POST'])
def getAllBattery():
    if request.method == 'POST':
        return BatteryHandler().insertBattery(request.json)
    else :
        if not request.args:
            return BatteryHandler().getAllBattery()
        else:
            return BatteryHandler().searchBattery(request.args)

@app.route('/DRL/battery/<int:battery_id>', methods = ['GET','PUT','DELETE']) 
def getBatteryById(battery_id):
    if request.method == 'GET':
        return BatteryHandler().getBatteryById(battery_id)
    elif request.method == 'PUT':
        return BatteryHandler().updateBattery(battery_id, request.json)
    elif request.method == 'DELETE':
        return BatteryHandler().deleteBaterry(battery_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/battery/available', methods = ['GET'])
def getAllAvailableBattery():
    return BatteryHandler().getAllAvailableBattery()

@app.route('/DRL/battery/reserved', methods = ['GET'])
def getAllReservedBattery():
    return BatteryHandler().getAllReservedBattery()

#################### Generator Routes ####################

@app.route('/DRL/generator',methods = ['GET','POST'])
def getAllGenerator():
    if request.method == 'POST':
        return GeneratorHandler().insertGenerator(request.json)
    else :
        if not request.args:
            return GeneratorHandler().getAllGenerator()
        else:
            return GeneratorHandler().searchGenerator(request.args)

@app.route('/DRL/generator/<int:generator_id>', methods = ['GET','PUT','DELETE'])
def getGeneratorById(generator_id):
    if request.method == 'GET':
        return GeneratorHandler().getGeneratorById(generator_id)
    elif request.method == 'PUT':
        return GeneratorHandler().updateGenerator(generator_id, request.json)
    elif request.method == 'DELETE':
        return GeneratorHandler().deleteGenerator(generator_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/generator/available',methods = ['GET'])
def getAllAvailableGenerator():
    return GeneratorHandler().getAllAvailableGenerator()

@app.route('/DRL/generator/reserved',methods = ['GET'])
def getAllReservedGenerator():
    return GeneratorHandler().getAllReservedGenerator()

if __name__ == '__main__':
    app.run(debug=True)

