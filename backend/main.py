from flask import Flask, jsonify, request
from handler.fuel import FuelHandler
from handler.tools import ToolHandler
from handler.food import FoodHandler
from handler.medicine import MedicineHandler
# from handler.reservation import ReservationHandler

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the DRL App!'

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

#################### Tools Routes ####################

@app.route("/DRL/tools", methods=['GET', 'POST'])
def getAllTools():
    if request.method == 'POST':
        return ToolHandler().insertTool(request.json)
    else:
        if not request.args:
            return ToolHandler().getAllTools()
        else:
            return ToolHandler().searchTool(request.args)

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
    return ToolHandler().getToolBySupplierId(supplier_id)

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

#################### Reservation Routes ####################
#
#

if __name__ == '__main__':
    app.run(debug=True)