from flask import Flask, jsonify, request
from handler.customer import CustomerHandler
from handler.water import WaterHandler
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
    return 'Hello, this is the parts DB App!'

@app.route("/DRL/customers", methods=['GET', 'POST'])
def getAllCustomers():
    if request.method == 'POST':
        return CustomerHandler().insertCustomer(request.json)
    else:
        if not request.args:
            return CustomerHandler().getAllCustomers()
        else:
            return CustomerHandler().searchCustomers(request.args)

@app.route('/DRL/customers/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def getCustomerById(customer_id):
    if request.method == 'GET':
        return CustomerHandler().getCustomerById(customer_id)
    elif request.method == 'PUT':
        return CustomerHandler().updateCustomer(customer_id, request.form)
    elif request.method == 'DELETE':
        return CustomerHandler().deleteCustomer(customer_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route("/DRL/water", methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        return WaterHandler().insertWater(request.json)
    else:
        if not request.args:
            return WaterHandler().getAllWater()
        else:
            return WaterHandler().searchWater(request.args)

@app.route('/DRL/water/<int:water_id>', methods=['GET', 'PUT', 'DELETE'])
def getWaterById(water_id):
    if request.method == 'GET':
        return WaterHandler().getWaterById(water_id)
    elif request.method == 'PUT':
        return WaterHandler().updateWater(water_id, request.form)
    elif request.method == 'DELETE':
        return WaterHandler().deleteWater(water_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/water/supplier/<int:supplier_id>', methods = ['GET'])
def getWaterBySupplierId(supplier_id):
    return WaterHandler().getWaterBySupplierId(supplier_id)

if __name__ == '__main__':
    app.run(debug=True)