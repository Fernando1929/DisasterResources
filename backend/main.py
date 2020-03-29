from flask import Flask, jsonify, request
from handler.fuel import FuelHandler
from handler.tools import ToolHandler
from handler.food import FoodHandler
from handler.medicine import MedicineHandler
from handler.address import AddressHandler
from handler.reservation import ReservationHandler
from handler.login import LoginHandler
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

@app.route('/DRL/fuel/<int:fuel_id>/address', methods=['GET'])
def getFuelAddress(fuel_id):
    return FuelHandler().getFuelAddress(fuel_id)

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

@app.route('/DRL/tools/<int:tool_id>/address', methods=['GET'])
def getToolAddress(tool_id):
    return ToolHandler().getToolAddress(tool_id)

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

@app.route('/DRL/food/<int:food_id>/address', methods=['GET'])
def getFoodAddress(food_id):
    return FoodHandler().getFoodAddress(food_id)

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

@app.route('/DRL/medicine/<int:med_id>/address', methods=['GET'])
def getMedicineAddress(med_id):
    return MedicineHandler().getMedicineAddress(med_id)

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