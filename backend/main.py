from flask import Flask, jsonify, request
from handler.customer import CustomerHandler
from handler.water import WaterHandler
from handler.cloth import ClothHandler
from handler.heavyEquip import HeavyEquipHandler
from handler.medDevice import MedDeviceHandler
from handler.request import RequestHandler
from handler.athMovil import AthMovilHandler
from handler.paypal import PaypalHandler
from handler.creditCard import CreditCardHandler
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

@app.route('/DRL/water/<int:water_id>/address', methods = ['GET'])
def getWaterAddress(water_id):
    return WaterHandler().getWaterAddress(water_id)

@app.route('/DRL/water/available', methods = ['GET'])
def getAllAvailableWater():
    return WaterHandler().getAllAvailableWater()

@app.route('/DRL/water/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableWaterBySupplierId(supplier_id):
    return WaterHandler().getAllAvailableWaterBySupplierId(supplier_id)

@app.route('/DRL/water/reserved', methods = ['GET'])
def getAllReservedWater():
    return WaterHandler().getAllReservedWater()

@app.route('/DRL/water/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedWaterBySupplierId(supplier_id):
    return WaterHandler().getAllReservedWaterBySupplierId(supplier_id)

@app.route('/DRL/water/requested', methods = ['GET'])
def getAllRequestedWater():
    return WaterHandler().getAllRequestedWater()

@app.route('/DRL/water/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedWaterBySupplierId(supplier_id):
    return WaterHandler().getAllRequestedWaterBySupplierId(supplier_id)

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

@app.route('/DRL/cloth/<int:cloth_id>/address', methods = ['GET'])
def getClothAddress(cloth_id):
    return ClothHandler().getClothAddress(cloth_id)

@app.route('/DRL/cloth/available', methods = ['GET'])
def getAllAvailableCloth():
    return ClothHandler().getAllAvailableCloth()

@app.route('/DRL/cloth/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableClothBySupplierId(supplier_id):
    return ClothHandler().getAllAvailableClothBySupplierId(supplier_id)

@app.route('/DRL/cloth/reserved', methods = ['GET'])
def getAllReservedCloth():
    return ClothHandler().getAllReservedCloth()

@app.route('/DRL/cloth/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedClothBySupplierId(supplier_id):
    return ClothHandler().getAllReservedClothBySupplierId(supplier_id)

@app.route('/DRL/cloth/requested', methods = ['GET'])
def getAllRequestedCloth():
    return ClothHandler().getAllRequestedCloth()

@app.route('/DRL/cloth/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedClothBySupplierId(supplier_id):
    return ClothHandler().getAllRequestedClothBySupplierId(supplier_id)

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

@app.route('/DRL/heavyequipment/<int:hequip_id>/address', methods = ['GET'])
def getHeavyEquipAddress(hequip_id):
    return HeavyEquipHandler().getHeavyEquipAddress(hequip_id)

@app.route('/DRL/heavyequipment/available', methods = ['GET'])
def getAllAvailableHeavyEquip():
    return HeavyEquipHandler().getAllAvailableHeavyEquip()

@app.route('/DRL/heavyequipment/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getAllAvailableHeavyEquipBySupplierId(supplier_id)

@app.route('/DRL/heavyequipment/reserved', methods = ['GET'])
def getAllReservedHeavyEquip():
    return HeavyEquipHandler().getAllReservedHeavyEquip()

@app.route('/DRL/heavyequipment/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getAllReservedHeavyEquipBySupplierId(supplier_id)

@app.route('/DRL/heavyequipment/requested', methods = ['GET'])
def getAllRequestedHeavyEquip():
    return HeavyEquipHandler().getAllRequestedHeavyEquip()

@app.route('/DRL/heavyequipment/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getAllRequestedHeavyEquipBySupplierId(supplier_id)

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

@app.route('/DRL/medicaldevice/<int:mdevice_id>/address', methods = ['GET'])
def getMedDeviceAddress(mdevice_id):
    return MedDeviceHandler().getMedDeviceAddress(mdevice_id)

@app.route('/DRL/medicaldevice/available', methods = ['GET'])
def getAllAvailablemedDevice():
    return MedDeviceHandler().getAllAvailableMedDevice()

@app.route('/DRL/medicaldevice/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableMedDeviceBySupplierId(supplier_id):
    return MedDeviceHandler().getAllAvailableMedDeviceBySupplierId(supplier_id)

@app.route('/DRL/medicaldevice/reserved', methods = ['GET'])
def getAllReservedMedDevice():
    return MedDeviceHandler().getAllReservedMedDevice()

@app.route('/DRL/medicaldevice/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedMedDeviceBySupplierId(supplier_id):
    return MedDeviceHandler().getAllReservedMedDeviceBySupplierId(supplier_id)

@app.route('/DRL/medicaldevice/requested', methods = ['GET'])
def getAllRequestedMedDevice():
    return MedDeviceHandler().getAllRequestedMedDevice()

@app.route('/DRL/medicaldevice/requested/supplier/<int:supplier_id>', methods = ['GET'])
def getAllRequestedMedDeviceBySupplierId(supplier_id):
    return MedDeviceHandler().getAllRequestedMedDeviceBySupplierId(supplier_id)

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

#################### Ath Movil Routes ####################

@app.route("/DRL/athmovil", methods=['GET', 'POST'])
def getAllAthMovil():
    if request.method == 'POST':
        return AthMovilHandler().insertAthMovil(request.json)
    else:
        if not request.args:
            return AthMovilHandler().getAllAthMovil()
        else:
            return AthMovilHandler().searchAthMovil(request.args)

@app.route('/DRL/athmovil/<int:ath_movil_id>', methods=['GET', 'PUT', 'DELETE'])
def getAthMovilById(ath_movil_id):
    if request.method == 'GET':
        return AthMovilHandler().getAthMovilById(ath_movil_id)
    elif request.method == 'PUT':
        return AthMovilHandler().updateAthMovil(ath_movil_id, request.json)
    elif request.method == 'DELETE':
        return AthMovilHandler().deleteAthMovil(ath_movil_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/user/<int:user_id>/athmovil", methods=['GET'])
def getAthMovilByUserId(user_id):
    return AthMovilHandler().getAthMovilByUserId(user_id)

#################### Paypal Routes ####################

@app.route("/DRL/paypal", methods=['GET', 'POST'])
def getAllPaypal():
    if request.method == 'POST':
        return PaypalHandler().insertPaypal(request.json)
    else:
        if not request.args:
            return PaypalHandler().getAllPaypal()
        else:
            return PaypalHandler().searchPaypal(request.args)

@app.route('/DRL/paypal/<int:paypal_id>', methods=['GET', 'PUT', 'DELETE'])
def getPaypalById(paypal_id):
    if request.method == 'GET':
        return PaypalHandler().getPaypalById(paypal_id)
    elif request.method == 'PUT':
        return PaypalHandler().updatePaypal(paypal_id, request.json)
    elif request.method == 'DELETE':
        return PaypalHandler().deletePaypal(paypal_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/user/<int:user_id>/paypal", methods=['GET'])
def getPaypalByUserId(user_id):
    return PaypalHandler().getPaypalByUserId(user_id)

#################### Credit Card Routes ####################

@app.route("/DRL/creditcard", methods=['GET', 'POST'])
def getAllCreditCard():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(request.json)
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCard()
        else:
            return CreditCardHandler().searchCreditCard(request.args)

@app.route('/DRL/creditcard/<int:creditcard_id>', methods=['GET', 'PUT', 'DELETE'])
def getCreditCardById(creditcard_id):
    if request.method == 'GET':
        return CreditCardHandler().getCreditCardById(creditcard_id)
    elif request.method == 'PUT':
        return CreditCardHandler().updateCreditCard(creditcard_id, request.json)
    elif request.method == 'DELETE':
        return CreditCardHandler().deleteCreditCard(creditcard_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/user/<int:user_id>/creditcard", methods=['GET'])
def getCreditCardByUserId(user_id):
    return CreditCardHandler().getCreditCardByUserId(user_id)

if __name__ == '__main__':
    app.run(debug=True)