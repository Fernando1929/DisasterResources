from flask import Flask, jsonify, request
from handler.fuel import FuelHandler
from handler.tools import ToolHandler
from handler.food import FoodHandler
from handler.medicine import MedicineHandler
from handler.address import AddressHandler
from handler.reservation import ReservationHandler
from handler.login import LoginHandler

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the DRL App!'


#################### Login Routes ####################
@app.route("/DRL/login", methods=['POST'])
def login():
    return LoginHandler().insertLogin(request.json)

@app.route("/DRL/login/<int:login_id>", methods=['GET', 'PUT', 'DELETE'])
def getLoginById(login_id):
    if request.method == 'GET':
        return LoginHandler().getLoginById(login_id)
    elif request.method == 'PUT':
        return LoginHandler().updateLogin(login_id, request.json)
    elif request.method == 'DELETE':
        return LoginHandler().deleteLogin(login_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/user/<int:user_id>/login", methods=['GET'])
def getLoginByUserId(user_id):
    return LoginHandler().getLoginByUserId(user_id)

#################### Address Routes ####################
@app.route("/DRL/user/address", methods=['GET', 'POST'])
def getAllAddresses():
    if request.method == 'POST':
        return AddressHandler().insertAddress(request.json)
    else:
        if not request.args:
            return AddressHandler().getAllAddresses()
        else:
            return AddressHandler().searchAddress(request.args)

@app.route("/DRL/user/address/<int:address_id>", methods=['GET', 'PUT', 'DELETE'])
def getAddressById(address_id):
    if request.method == 'GET':
        return AddressHandler().getAddressById(address_id)
    elif request.method == 'PUT':
        return AddressHandler().updateAddress(address_id, request.json)
    elif request.method == 'DELETE':
        return AddressHandler().deleteAddress(address_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/user/<int:user_id>/address", methods=['GET'])
def getAddressesByUserId(user_id):
    return AddressHandler().getAddressesByUserId(user_id)

#################### Reservation Routes ####################
@app.route("/DRL/customer/reservation", methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        return ReservationHandler().insertReservation(request.json)
    else:
        if not request.args:
            return ReservationHandler().getAllReservations()
        else:
            return ReservationHandler().searchReservation(request.args)

@app.route("/DRL/customer/reservation/<int:reservation_id>", methods=['GET', 'PUT', 'DELETE'])
def getReservationById(reservation_id):
    if request.method == 'GET':
        return ReservationHandler().getReservationById(reservation_id)
    elif request.method == 'PUT':
        return ReservationHandler().updateReservation(reservation_id, request.json)
    elif request.method == 'DELETE':
        return ReservationHandler().deleteReservation(reservation_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/customer/<int:customer_id>/reservation", methods=['GET'])
def getReservationsByCustomerId(customer_id):
    return ReservationHandler().getReservationsByCustomerId(customer_id)

#################### Fuel Routes ####################

@app.route("/DRL/fuel", methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        return FuelHandler().insertFuel(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuels()
        else:
            return FuelHandler().searchFuel(request.args)

@app.route('/DRL/fuel/<int:fuel_id>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fuel_id):
    if request.method == 'GET':
        return FuelHandler().getFuelById(fuel_id)
    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fuel_id, request.json)
    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fuel_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/fuel/supplier/<int:supplier_id>', methods = ['GET'])
def getFuelBySupplierId(supplier_id):
    return FuelHandler().getFuelBySupplierId(supplier_id)

@app.route('/DRL/fuel/available', methods = ['GET'])
def getAllAvailableFuels():
    return FuelHandler().getAllAvailableFuels()

@app.route('/DRL/fuel/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableFuelBySupplierId(supplier_id):
    return FuelHandler().getAllAvailableFuelBySupplierId(supplier_id)

@app.route('/DRL/fuel/reserved', methods = ['GET'])
def getAllReservedFuels():
    return FuelHandler().getAllReservedFuels()

@app.route('/DRL/fuel/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedFuelBySupplierId(supplier_id):
    return FuelHandler().getAllReservedFuelBySupplierId(supplier_id)


#################### Tools Routes ####################

@app.route("/DRL/tools", methods=['GET', 'POST'])
def getAllTools():
    if request.method == 'POST':
        return ToolHandler().insertTool(request.json)
    else:
        if not request.args:
            return ToolHandler().getAllTools()
        else:
            return ToolHandler().searchTools(request.args)

@app.route('/DRL/tools/<int:tool_id>', methods=['GET', 'PUT', 'DELETE'])
def getToolById(tool_id):
    if request.method == 'GET':
        return ToolHandler().getToolById(tool_id)
    elif request.method == 'PUT':
        return ToolHandler().updateTool(tool_id, request.json)
    elif request.method == 'DELETE':
        return ToolHandler().deleteTool(tool_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/tools/supplier/<int:supplier_id>', methods = ['GET'])
def getToolBySupplierId(supplier_id):
    return ToolHandler().getToolsBySupplierId(supplier_id)

@app.route('/DRL/tools/available', methods = ['GET'])
def getAllAvailableTools():
    return ToolHandler().getAllAvailableTools()

@app.route('/DRL/tools/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableToolsBySupplierId(supplier_id):
    return ToolHandler().getAllAvailableToolsBySupplierId(supplier_id)

@app.route('/DRL/tools/reserved', methods = ['GET'])
def getAllReservedTools():
    return ToolHandler().getAllReservedTools()

@app.route('/DRL/tools/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedToolsBySupplierId(supplier_id):
    return ToolHandler().getAllReservedToolsBySupplierId(supplier_id)

#################### Food Routes ####################

@app.route("/DRL/food", methods=['GET', 'POST'])
def getAllFoods():
    if request.method == 'POST':
        return FoodHandler().insertFood(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFoods()
        else:
            return FoodHandler().searchFood(request.args)

@app.route('/DRL/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updateFood(food_id, request.json)
    elif request.method == 'DELETE':
        return FoodHandler().deleteFood(food_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/food/supplier/<int:supplier_id>', methods = ['GET'])
def getFoodBySupplierId(supplier_id):
    return FoodHandler().getFoodBySupplierId(supplier_id)

@app.route('/DRL/food/available', methods = ['GET'])
def getAllAvailableFoods():
    return FoodHandler().getAllAvailableFoods()

@app.route('/DRL/food/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllAvailableFoodBySupplierId(supplier_id)

@app.route('/DRL/food/reserved', methods = ['GET'])
def getAllReservedFoods():
    return FoodHandler().getAllReservedFoods()

@app.route('/DRL/food/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllReservedFoodBySupplierId(supplier_id)

#################### Medicine Routes ####################

@app.route("/DRL/medicine", methods=['GET', 'POST'])
def getAllMedicines():
    if request.method == 'POST':
        return MedicineHandler().insertMedicine(request.json)
    else:
        if not request.args:
            return MedicineHandler().getAllMedicines()
        else:
            return MedicineHandler().searchMedicine(request.args)

@app.route('/DRL/medicine/<int:med_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicineById(med_id):
    if request.method == 'GET':
        return MedicineHandler().getMedicineById(med_id)
    elif request.method == 'PUT':
        return MedicineHandler().updateMedicine(med_id, request.json)
    elif request.method == 'DELETE':
        return MedicineHandler().deleteMedicine(med_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/medicine/supplier/<int:supplier_id>', methods = ['GET'])
def getMedicineBySupplierId(supplier_id):
    return MedicineHandler().getMedicineBySupplierId(supplier_id)

@app.route('/DRL/medicine/available', methods = ['GET'])
def getAllAvailableMedicines():
    return MedicineHandler().getAllAvailableMedicines()

@app.route('/DRL/medicine/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllAvailableMedicineBySupplierId(supplier_id)

@app.route('/DRL/medicine/reserved', methods = ['GET'])
def getAllReservedMedicines():
    return MedicineHandler().getAllReservedMedicines()

@app.route('/DRL/medicine/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllReservedMedicineBySupplierId(supplier_id)



if __name__ == '__main__':
    app.run(debug=True)