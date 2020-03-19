from flask import Flask, jsonify, request
from handler.customer import CustomerHandler
from handler.water import WaterHandler
from handler.cloth import ClothHandler
from handler.heavyequip import HeavyEquipHandler
from handler.medDevice import MedDeviceHandler
from handler.request import RequestHandler
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

#################### Customer Routes ####################

@app.route("/DRL/customer", methods=['GET', 'POST'])
def getAllCustomers():
    if request.method == 'POST':
        return CustomerHandler().insertCustomer(request.json)
    else:
        if not request.args:
            return CustomerHandler().getAllCustomer()
        else:
            return CustomerHandler().searchCustomer(request.args)

@app.route('/DRL/customer/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def getCustomerById(customer_id):
    if request.method == 'GET':
        return CustomerHandler().getCustomerById(customer_id)
    elif request.method == 'PUT':
        return CustomerHandler().updateCustomer(customer_id, request.json)
    elif request.method == 'DELETE':
        return CustomerHandler().deleteCustomer(customer_id)
    else:
        return jsonify(Error="Method not allowed."), 405

#################### Water Routes ####################

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
        return WaterHandler().updateWater(water_id, request.json)
    elif request.method == 'DELETE':
        return WaterHandler().deleteWater(water_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/water/supplier/<int:supplier_id>', methods = ['GET'])
def getWaterBySupplierId(supplier_id):
    return WaterHandler().getWaterBySupplierId(supplier_id)

@app.route('/DRL/water/available', methods = ['GET'])
def getAllAvailableWater():
    return WaterHandler().getAllAvailableWater()

@app.route('/DRL/water/reserved', methods = ['GET'])
def getAllReservedWater():
    return WaterHandler().getAllReservedWater()

#################### Cloth Routes ####################

@app.route("/DRL/cloth", methods=['GET', 'POST'])
def getAllCloth():
    if request.method == 'POST':
        return ClothHandler().insertCloth(request.json)
    else:
        if not request.args:
            return ClothHandler().getAllCloth()
        else:
            return ClothHandler().searchCloth(request.args)

@app.route('/DRL/cloth/<int:cloth_id>', methods=['GET', 'PUT', 'DELETE'])
def getClothById(cloth_id):
    if request.method == 'GET':
        return ClothHandler().getClothById(cloth_id)
    elif request.method == 'PUT':
        return ClothHandler().updateCloth(cloth_id, request.json)
    elif request.method == 'DELETE':
        return ClothHandler().deleteCloth(cloth_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/cloth/supplier/<int:supplier_id>', methods = ['GET'])
def getClothBySupplierId(supplier_id):
    return ClothHandler().getClothBySupplierId(supplier_id)

@app.route('/DRL/cloth/available', methods = ['GET'])
def getAllAvailableCloth():
    return ClothHandler().getAllAvailableCloth()

@app.route('/DRL/cloth/reserved', methods = ['GET'])
def getAllReservedCloth():
    return ClothHandler().getAllReservedCloth()

#################### Heavy Equipment Routes ####################

@app.route("/DRL/heavyequipment", methods=['GET', 'POST'])
def getAllHeavyEquip():
    if request.method == 'POST':
        return HeavyEquipHandler().insertHeavyEquip(request.json)
    else:
        if not request.args:
            return HeavyEquipHandler().getAllHeavyEquip()
        else:
            return HeavyEquipHandler().searchHeavyEquip(request.args)

@app.route('/DRL/heavyequipment/<int:hequip_id>', methods=['GET', 'PUT', 'DELETE'])
def getHeavyEquipById(hequip_id):
    if request.method == 'GET':
        return HeavyEquipHandler().getHeavyEquipById(hequip_id)
    elif request.method == 'PUT':
        return HeavyEquipHandler().updateHeavyEquip(hequip_id, request.json)
    elif request.method == 'DELETE':
        return HeavyEquipHandler().deleteHeavyEquip(hequip_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/heavyequipment/supplier/<int:supplier_id>', methods = ['GET'])
def getHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getHeavyEquipBySupplierId(supplier_id)

@app.route('/DRL/heavyequipment/available', methods = ['GET'])
def getAllAvailableHeavyEquip():
    return HeavyEquipHandler().getAllAvailableHeavyEquip()

@app.route('/DRL/heavyequipment/reserved', methods = ['GET'])
def getAllReservedHeavyEquip():
    return HeavyEquipHandler().getAllReservedHeavyEquip()

#################### Medical Device Routes ####################

@app.route("/DRL/medicaldevice", methods=['GET', 'POST'])
def getAllMedDevice():
    if request.method == 'POST':
        return MedDeviceHandler().insertMedDevice(request.json)
    else:
        if not request.args:
            return MedDeviceHandler().getAllMedDevice()
        else:
            return MedDeviceHandler().searchMedDevice(request.args)

@app.route('/DRL/medicaldevice/<int:mdevice_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedDeviceById(mdevice_id):
    if request.method == 'GET':
        return MedDeviceHandler().getMedDeviceById(mdevice_id)
    elif request.method == 'PUT':
        return MedDeviceHandler().updateMedDevice(mdevice_id, request.json)
    elif request.method == 'DELETE':
        return MedDeviceHandler().deleteMedDevice(mdevice_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/medicaldevice/supplier/<int:supplier_id>', methods = ['GET'])
def getMedDeviceBySupplierId(supplier_id):
    return MedDeviceHandler().getMedDeviceBySupplierId(supplier_id)

@app.route('/DRL/medicaldevice/available', methods = ['GET'])
def getAllAvailablemedDevice():
    return MedDeviceHandler().getAllAvailableMedDevice()

@app.route('/DRL/medicaldevice/reserved', methods = ['GET'])
def getAllReservedMedDevice():
    return MedDeviceHandler().getAllReservedMedDevice()

#################### Request Routes ####################

@app.route('/DRL/customer/request', methods= ['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.json)
    else:
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchRequest(request.args)

@app.route('/DRL/customer/request/<int:request_id>', methods= ['GET', 'PUT', 'DELETE'])
def getRequestById(request_id):
    if request.method == 'GET':
        return RequestHandler().getRequestById(request_id)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(request_id, request.json)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequest(request_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/customer/<int:customer_id>/request', methods= ['GET'])
def getRequestByCustomerId(customer_id):
    return RequestHandler().getRequestByCustomerId(customer_id)

if __name__ == '__main__':
    app.run(debug=True)