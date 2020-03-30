from flask import Flask, jsonify, request
from handler.fuel import FuelHandler
from handler.tools import ToolHandler
from handler.food import FoodHandler
from handler.medicine import MedicineHandler
from handler.address import AddressHandler
from handler.reservation import ReservationHandler
from handler.login import LoginHandler
from handler.resource import ResourceHandler

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the DRL App!'

@app.route("/DRL/resources", methods=['GET']) 
def getAllResources():
    return ResourceHandler().getAllResources()

@app.route("/DRL/resources/<int:resource_id>", methods=['GET'])
def getResourceById(resource_id):
    return ResourceHandler().getResourceById(resource_id)

@app.route("/DRL/resources/<int:resource_id>/fullinfo", methods=['GET'])
def getResourceFullInfo(resource_id):
    return ResourceHandler().getResourceFullInfo(resource_id)

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

@app.route("/DRL/resources/fuel", methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        return FuelHandler().insertFuel(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuels()
        else:
            return FuelHandler().searchFuel(request.args)

@app.route('/DRL/resources/fuel/<int:fuel_id>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fuel_id):
    if request.method == 'GET':
        return FuelHandler().getFuelById(fuel_id)
    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fuel_id, request.json)
    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fuel_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/fuel/<int:fuel_id>/address', methods=['GET'])
def getFuelAddress(fuel_id):
    return FuelHandler().getFuelAddress(fuel_id)

@app.route('/DRL/resources/fuel/supplier/<int:supplier_id>', methods = ['GET'])
def getFuelBySupplierId(supplier_id):
    return FuelHandler().getFuelBySupplierId(supplier_id)

@app.route('/DRL/resources/fuel/available', methods = ['GET'])
def getAllAvailableFuels():
    return FuelHandler().getAllAvailableFuels()

@app.route('/DRL/resources/fuel/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableFuelBySupplierId(supplier_id):
    return FuelHandler().getAllAvailableFuelBySupplierId(supplier_id)

@app.route('/DRL/resources/fuel/reserved', methods = ['GET'])
def getAllReservedFuels():
    return FuelHandler().getAllReservedFuels()

@app.route('/DRL/resources/fuel/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedFuelBySupplierId(supplier_id):
    return FuelHandler().getAllReservedFuelBySupplierId(supplier_id)

@app.route('/DRL/resources/fuel/requested', methods = ['GET'])
def getAllRequestedFuels():
    return FuelHandler().getAllRequestedFuels()

@app.route('/DRL/resources/fuel/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedFuelBySupplierId(supplier_id):
    return FuelHandler().getAllRequestedFuelBySupplierId(supplier_id)


#################### Tools Routes ####################

@app.route("/DRL/resources/tools", methods=['GET', 'POST'])
def getAllTools():
    if request.method == 'POST':
        return ToolHandler().insertTool(request.json)
    else:
        if not request.args:
            return ToolHandler().getAllTools()
        else:
            return ToolHandler().searchTools(request.args)

@app.route('/DRL/resources/tools/<int:tool_id>', methods=['GET', 'PUT', 'DELETE'])
def getToolById(tool_id):
    if request.method == 'GET':
        return ToolHandler().getToolById(tool_id)
    elif request.method == 'PUT':
        return ToolHandler().updateTool(tool_id, request.json)
    elif request.method == 'DELETE':
        return ToolHandler().deleteTool(tool_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/tools/<int:tool_id>/address', methods=['GET'])
def getToolAddress(tool_id):
    return ToolHandler().getToolAddress(tool_id)

@app.route('/DRL/resources/tools/supplier/<int:supplier_id>', methods = ['GET'])
def getToolBySupplierId(supplier_id):
    return ToolHandler().getToolsBySupplierId(supplier_id)

@app.route('/DRL/resources/tools/available', methods = ['GET'])
def getAllAvailableTools():
    return ToolHandler().getAllAvailableTools()

@app.route('/DRL/resources/tools/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableToolsBySupplierId(supplier_id):
    return ToolHandler().getAllAvailableToolsBySupplierId(supplier_id)

@app.route('/DRL/resources/tools/reserved', methods = ['GET'])
def getAllReservedTools():
    return ToolHandler().getAllReservedTools()

@app.route('/DRL/resources/tools/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedToolsBySupplierId(supplier_id):
    return ToolHandler().getAllReservedToolsBySupplierId(supplier_id)

@app.route('/DRL/resources/tools/requested', methods = ['GET'])
def getAllRequestedTools():
    return ToolHandler().getAllRequestedTools()

@app.route('/DRL/resources/tools/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedToolsBySupplierId(supplier_id):
    return ToolHandler().getAllRequestedToolsBySupplierId(supplier_id)

#################### Food Routes ####################

@app.route("/DRL/resources/food", methods=['GET', 'POST'])
def getAllFoods():
    if request.method == 'POST':
        return FoodHandler().insertFood(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFoods()
        else:
            return FoodHandler().searchFood(request.args)

@app.route('/DRL/resources/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updateFood(food_id, request.json)
    elif request.method == 'DELETE':
        return FoodHandler().deleteFood(food_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/food/<int:food_id>/address', methods=['GET'])
def getFoodAddress(food_id):
    return FoodHandler().getFoodAddress(food_id)

@app.route('/DRL/resources/food/supplier/<int:supplier_id>', methods = ['GET'])
def getFoodBySupplierId(supplier_id):
    return FoodHandler().getFoodBySupplierId(supplier_id)

@app.route('/DRL/resources/food/available', methods = ['GET'])
def getAllAvailableFoods():
    return FoodHandler().getAllAvailableFoods()

@app.route('/DRL/resources/food/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllAvailableFoodBySupplierId(supplier_id)

@app.route('/DRL/resources/food/reserved', methods = ['GET'])
def getAllReservedFoods():
    return FoodHandler().getAllReservedFoods()

@app.route('/DRL/resources/food/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllReservedFoodBySupplierId(supplier_id)

@app.route('/DRL/resources/food/requested', methods = ['GET'])
def getAllRequestedFoods():
    return FoodHandler().getAllRequestedFoods()

@app.route('/DRL/resources/food/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllRequestedFoodBySupplierId(supplier_id)

#################### Medicine Routes ####################

@app.route("/DRL/resources/medicine", methods=['GET', 'POST'])
def getAllMedicines():
    if request.method == 'POST':
        return MedicineHandler().insertMedicine(request.json)
    else:
        if not request.args:
            return MedicineHandler().getAllMedicines()
        else:
            return MedicineHandler().searchMedicine(request.args)

@app.route('/DRL/resources/medicine/<int:med_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicineById(med_id):
    if request.method == 'GET':
        return MedicineHandler().getMedicineById(med_id)
    elif request.method == 'PUT':
        return MedicineHandler().updateMedicine(med_id, request.json)
    elif request.method == 'DELETE':
        return MedicineHandler().deleteMedicine(med_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/medicine/<int:med_id>/address', methods=['GET'])
def getMedicineAddress(med_id):
    return MedicineHandler().getMedicineAddress(med_id)

@app.route('/DRL/resources/medicine/supplier/<int:supplier_id>', methods = ['GET'])
def getMedicineBySupplierId(supplier_id):
    return MedicineHandler().getMedicineBySupplierId(supplier_id)

@app.route('/DRL/resources/medicine/available', methods = ['GET'])
def getAllAvailableMedicines():
    return MedicineHandler().getAllAvailableMedicines()

@app.route('/DRL/resources/medicine/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllAvailableMedicineBySupplierId(supplier_id)

@app.route('/DRL/resources/medicine/reserved', methods = ['GET'])
def getAllReservedMedicines():
    return MedicineHandler().getAllReservedMedicines()

@app.route('/DRL/resources/medicine/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllReservedMedicineBySupplierId(supplier_id)

@app.route('/DRL/resources/medicine/requested', methods = ['GET'])
def getAllRequestedMedicines():
    return MedicineHandler().getAllReservedMedicines()

@app.route('/DRL/resources/medicine/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllRequestedMedicineBySupplierId(supplier_id)



if __name__ == '__main__':
    app.run(debug=True)