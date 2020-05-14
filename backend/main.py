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
from handler.heavyequip import HeavyEquipHandler
from handler.medDevice import MedDeviceHandler
from handler.request import RequestHandler
from handler.athMovil import AthMovilHandler
from handler.paypal import PaypalHandler
from handler.creditCard import CreditCardHandler
from handler.ice import IceHandler
from handler.supplier import SupplierHandler
from handler.admin import AdminHandler
from handler.order import OrderHandler
from handler.generator import GeneratorHandler
from handler.battery import BatteryHandler
from handler.company import CompanyHandler
from handler.resource import ResourceHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return 'Welcome to the Disaster Resources Locator App!'

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
            return AddressHandler().searchAddresses(request.args)

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

#################### Customer Routes ####################

@app.route("/DRL/register/customer", methods=['POST'])
def registerCustomer():
    return CustomerHandler().insertCustomer(request.json)

@app.route("/DRL/customer", methods=['GET'])
def getAllCustomers():
    if not request.args:
        return CustomerHandler().getAllCustomers()
    else:
        return CustomerHandler().searchCustomers(request.args)

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

#################### Supplier Routes ####################

@app.route("/DRL/register/supplier", methods=['POST'])
def registerSupplier():
    return SupplierHandler().insertSupplier(request.json)

@app.route('/DRL/supplier', methods = ['GET'])
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

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

@app.route('/DRL/supplier/company/<int:company_id>', methods=["GET"])
def getSuppliersByCompanyId(company_id):
    return SupplierHandler().getSuppliersByCompanyId(company_id)

#################### Admin Routes ####################

@app.route("/DRL/register/admin", methods=['POST'])
def registerAdmin():
    return AdminHandler().insertAdmin(request.json)

@app.route('/DRL/admin', methods = ['GET'])
def getAllAdmins():
    if not request.args:
        return AdminHandler().getAllAdmins()
    else:
        return AdminHandler().searchAdmins(request.args)

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

#################### Company Routes ####################

@app.route('/DRL/company', methods = ['GET','POST'])
def getAllCompanies():
    if request.method == 'POST':
        return CompanyHandler().insertCompany(request.json)
    else :
        if not request.args:
            return CompanyHandler().getAllCompanies()
        else:
            return CompanyHandler().searchCompany(request.args)

@app.route('/DRL/company/<int:company_id>', methods = ['GET','PUT','DELETE'])
def getCompanyById(company_id):
    if request.method == 'GET':
        return CompanyHandler().getCompanyById(company_id)
    elif request.method == 'PUT':
        return CompanyHandler().updateCompany(company_id, request.json)
    elif request.method == 'DELETE':
        return CompanyHandler().deleteCompany(company_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/supplier/<int:supplier_id>/company', methods = ['GET'])
def getCompanyBySupplierId(supplier_id):
    return CompanyHandler().getCompanyBySupplierId(supplier_id)

#################### Request Routes ####################

@app.route('/DRL/customer/requests', methods= ['GET', 'POST'])
def getAllRequests():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.json)
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequests(request.args)

@app.route('/DRL/customer/requests/<int:request_id>', methods= ['GET', 'PUT', 'DELETE'])
def getRequestById(request_id):
    if request.method == 'GET':
        return RequestHandler().getRequestById(request_id)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(request_id, request.json)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequest(request_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/customer/<int:customer_id>/requests', methods= ['GET'])
def getRequestsByCustomerId(customer_id):
    return RequestHandler().getRequestsByCustomerId(customer_id)

#################### Reservation Routes ####################

@app.route("/DRL/customer/reservations", methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        return ReservationHandler().insertReservation(request.json)
    else:
        if not request.args:
            return ReservationHandler().getAllReservations()
        else:
            return ReservationHandler().searchReservations(request.args)

@app.route("/DRL/customer/reservations/<int:reservation_id>", methods=['GET', 'PUT', 'DELETE'])
def getReservationById(reservation_id):
    if request.method == 'GET':
        return ReservationHandler().getReservationById(reservation_id)
    elif request.method == 'PUT':
        return ReservationHandler().updateReservation(reservation_id, request.json)
    elif request.method == 'DELETE':
        return ReservationHandler().deleteReservation(reservation_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/customer/reservations/<int:reservation_id>/resources", methods=['GET'])
def getResourcesByReservationId(reservation_id):
    return ReservationHandler().getResourcesByReservationId(reservation_id)

@app.route("/DRL/customer/<int:customer_id>/reservations", methods=['GET'])
def getReservationsByCustomerId(customer_id):
    return ReservationHandler().getReservationsByCustomerId(customer_id)

#################### Order Routes ####################

@app.route('/DRL/customer/orders', methods=['GET','POST'])
def getAllOrder():
    if request.method == 'POST':
        return OrderHandler().insertOrder(request.json)
    else:
        if not request.args:
            return OrderHandler().getAllOrders()
        else:
            return OrderHandler().searchOrders(request.args)

@app.route('/DRL/customer/orders/<int:order_id>', methods=['GET', 'PUT','DELETE'])
def getOrderById(order_id):
    if request.method == 'GET':
        return OrderHandler().getOrderById(order_id)
    elif request.method == 'PUT':
        return OrderHandler().updateOrder(order_id, request.json)
    elif request.method == 'DELETE':
        return OrderHandler().deleteOrder(order_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DRL/customer/orders/<int:order_id>/resources', methods=['GET'])
def getResourcesByOrderId(order_id):
    return OrderHandler().getResourcesByOrderId(order_id)

@app.route('/DRL/customer/orders/<int:order_id>/payment', methods=['GET'])
def getPaymentByOrderId(order_id):
    return OrderHandler().getPaymentByOrderId(order_id)

@app.route('/DRL/customer/<int:customer_id>/orders', methods=['GET'])
def getOrderByCustomerId(customer_id):
    return OrderHandler().getOrderByCustomerId(customer_id)

#################### Credit Card Routes ####################

@app.route("/DRL/customer/creditcard", methods=['GET', 'POST'])
def getAllCreditCards():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(request.json)
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCards()
        else:
            return CreditCardHandler().searchCreditCard(request.args)

@app.route('/DRL/customer/creditcard/<int:creditcard_id>', methods=['GET', 'PUT', 'DELETE'])
def getCreditCardById(creditcard_id):
    if request.method == 'GET':
        return CreditCardHandler().getCreditCardById(creditcard_id)
    elif request.method == 'PUT':
        return CreditCardHandler().updateCreditCard(creditcard_id, request.json)
    elif request.method == 'DELETE':
        return CreditCardHandler().deleteCreditCard(creditcard_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/customer/<int:customer_id>/creditcard", methods=['GET'])
def getCreditCardByCustomerId(customer_id):
    return CreditCardHandler().getCreditCardByCustomerId(customer_id)

#################### Ath Movil Routes ####################

@app.route("/DRL/customer/athmovil", methods=['GET', 'POST'])
def getAllAthMovil():
    if request.method == 'POST':
        return AthMovilHandler().insertAthMovil(request.json)
    else:
        if not request.args:
            return AthMovilHandler().getAllAthMovil()
        else:
            return AthMovilHandler().searchAthMovil(request.args)

@app.route('/DRL/customer/athmovil/<int:ath_movil_id>', methods=['GET', 'PUT', 'DELETE'])
def getAthMovilById(ath_movil_id):
    if request.method == 'GET':
        return AthMovilHandler().getAthMovilById(ath_movil_id)
    elif request.method == 'PUT':
        return AthMovilHandler().updateAthMovil(ath_movil_id, request.json)
    elif request.method == 'DELETE':
        return AthMovilHandler().deleteAthMovil(ath_movil_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/customer/<int:customer_id>/athmovil", methods=['GET'])
def getAthMovilByCustomerId(customer_id):
    return AthMovilHandler().getAthMovilByCustomerId(customer_id)

#################### Paypal Routes ####################

@app.route("/DRL/customer/paypal", methods=['GET', 'POST'])
def getAllPaypal():
    if request.method == 'POST':
        return PaypalHandler().insertPaypal(request.json)
    else:
        if not request.args:
            return PaypalHandler().getAllPaypal()
        else:
            return PaypalHandler().searchPaypal(request.args)

@app.route('/DRL/customer/paypal/<int:paypal_id>', methods=['GET', 'PUT', 'DELETE'])
def getPaypalById(paypal_id):
    if request.method == 'GET':
        return PaypalHandler().getPaypalById(paypal_id)
    elif request.method == 'PUT':
        return PaypalHandler().updatePaypal(paypal_id, request.json)
    elif request.method == 'DELETE':
        return PaypalHandler().deletePaypal(paypal_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route("/DRL/customer/<int:customer_id>/paypal", methods=['GET'])
def getPaypalByCustomerId(customer_id):
    return PaypalHandler().getPaypalByCustomerId(customer_id)

#################### General Resource Routes ####################

@app.route("/DRL/resources", methods=['GET']) 
def getAllResources():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResources(request.args)

@app.route("/DRL/resources/<int:resource_id>", methods=['GET'])
def getResourceById(resource_id):
    return ResourceHandler().getResourceById(resource_id)

@app.route("/DRL/resources/<int:resource_id>/fullinfo", methods=['GET'])
def getResourceFullInfo(resource_id):
    return ResourceHandler().getResourceFullInfo(resource_id)

#################### Fuel Routes ####################

@app.route("/DRL/resources/fuel", methods=['GET', 'POST'])
def getAllFuels():
    if request.method == 'POST':
        return FuelHandler().insertFuel(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuels()
        else:
            return FuelHandler().searchFuels(request.args)

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
def getFuelsBySupplierId(supplier_id):
    return FuelHandler().getFuelsBySupplierId(supplier_id)

@app.route('/DRL/resources/fuel/available', methods = ['GET'])
def getAllAvailableFuels():
    return FuelHandler().getAllAvailableFuels()

@app.route('/DRL/resources/fuel/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableFuelsBySupplierId(supplier_id):
    return FuelHandler().getAllAvailableFuelsBySupplierId(supplier_id)

@app.route('/DRL/resources/fuel/reserved', methods = ['GET'])
def getAllReservedFuels():
    return FuelHandler().getAllReservedFuels()

@app.route('/DRL/resources/fuel/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedFuelsBySupplierId(supplier_id):
    return FuelHandler().getAllReservedFuelsBySupplierId(supplier_id)

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
def getToolsBySupplierId(supplier_id):
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

#################### Food Routes ####################

@app.route("/DRL/resources/food", methods=['GET', 'POST'])
def getAllFoods():
    if request.method == 'POST':
        return FoodHandler().insertFood(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFoods()
        else:
            return FoodHandler().searchFoods(request.args)

@app.route('/DRL/resources/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updateFood(food_id, request.json)
    elif request.method == 'DELETE':
        return FoodHandler().deleteFood(food_id)

@app.route('/DRL/resources/food/<int:food_id>/address', methods=['GET'])
def getFoodAddress(food_id):
    return FoodHandler().getFoodAddress(food_id)

@app.route('/DRL/resources/food/supplier/<int:supplier_id>', methods = ['GET'])
def getFoodsBySupplierId(supplier_id):
    return FoodHandler().getFoodsBySupplierId(supplier_id)

@app.route('/DRL/resources/food/available', methods = ['GET'])
def getAllAvailableFoods():
    return FoodHandler().getAllAvailableFoods()

@app.route('/DRL/resources/food/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllAvailableFoodsBySupplierId(supplier_id)

@app.route('/DRL/resources/food/reserved', methods = ['GET'])
def getAllReservedFoods():
    return FoodHandler().getAllReservedFoods()

@app.route('/DRL/resources/food/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedFoodsBySupplierId(supplier_id):
    return FoodHandler().getAllReservedFoodsBySupplierId(supplier_id)

#################### Medicine Routes ####################

@app.route("/DRL/resources/medicine", methods=['GET', 'POST'])
def getAllMedicines():
    if request.method == 'POST':
        return MedicineHandler().insertMedicine(request.json)
    else:
        if not request.args:
            return MedicineHandler().getAllMedicines()
        else:
            return MedicineHandler().searchMedicines(request.args)

@app.route('/DRL/resources/medicine/<int:med_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicineById(med_id):
    if request.method == 'GET':
        return MedicineHandler().getMedicineById(med_id)
    elif request.method == 'PUT':
        return MedicineHandler().updateMedicine(med_id, request.json)
    elif request.method == 'DELETE':
        return MedicineHandler().deleteMedicine(med_id)

@app.route('/DRL/resources/medicine/<int:med_id>/address', methods=['GET'])
def getMedicineAddress(med_id):
    return MedicineHandler().getMedicineAddress(med_id)

@app.route('/DRL/resources/medicine/supplier/<int:supplier_id>', methods = ['GET'])
def getMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getMedicinesBySupplierId(supplier_id)

@app.route('/DRL/resources/medicine/available', methods = ['GET'])
def getAllAvailableMedicines():
    return MedicineHandler().getAllAvailableMedicines()

@app.route('/DRL/resources/medicine/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllAvailableMedicinesBySupplierId(supplier_id)

@app.route('/DRL/resources/medicine/reserved', methods = ['GET'])
def getAllReservedMedicines():
    return MedicineHandler().getAllReservedMedicines()

@app.route('/DRL/resources/medicine/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedMedicinesBySupplierId(supplier_id):
    return MedicineHandler().getAllReservedMedicinesBySupplierId(supplier_id)

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

@app.route('/DRL/resources/ice/supplier/<int:supplier_id>', methods = ['GET'])
def getIceBySupplierId(supplier_id):
    return IceHandler().getIceBySupplierId(supplier_id)

@app.route('/DRL/resources/ice/<int:ice_id>/address', methods = ['GET'])
def getIceAddress(ice_id):
    return IceHandler().getIceAddress(ice_id)

@app.route('/DRL/resources/ice/available', methods = ['GET'])
def getAllAvailableIce():
    return IceHandler().getAllAvailableIce()

@app.route('/DRL/resources/ice/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableIceBySupplierId(supplier_id):
    return IceHandler().getAllAvailableIceBySupplierId(supplier_id)

@app.route('/DRL/resources/ice/reserved', methods = ['GET'])
def getAllReservedIce():
    return IceHandler().getAllReservedIce()

@app.route('/DRL/resources/ice/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedIceBySupplierId(supplier_id):
    return IceHandler().getAllReservedIceBySupplierId(supplier_id)

#################### Battery Routes ####################

@app.route('/DRL/resources/battery', methods = ['GET','POST'])
def getAllBatteries():
    if request.method == 'POST':
        return BatteryHandler().insertBattery(request.json)
    else :
        if not request.args:
            return BatteryHandler().getAllBatteries()
        else:
            return BatteryHandler().searchBatteries(request.args)

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

@app.route('/DRL/resources/battery/supplier/<int:supplier_id>', methods = ['GET'])
def getBatteriesBySupplierId(supplier_id):
    return BatteryHandler().getBatteriesBySupplierId(supplier_id)

@app.route('/DRL/resources/battery/<int:battery_id>/address', methods = ['GET'])
def getBatterAddress(battery_id):
    return BatteryHandler().getBatteryAddress(battery_id)

@app.route('/DRL/resources/battery/available', methods = ['GET'])
def getAllAvailableBatteries():
    return BatteryHandler().getAllAvailableBatteries()

@app.route('/DRL/resources/battery/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableBatteriesBySupplierId(supplier_id):
    return BatteryHandler().getAllAvailableBatteriesBySupplierId(supplier_id)

@app.route('/DRL/resources/battery/reserved', methods = ['GET'])
def getAllReservedBatteries():
    return BatteryHandler().getAllReservedBatteries()

@app.route('/DRL/resources/battery/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedBatteriesBySupplierId(supplier_id):
    return BatteryHandler().getAllReservedBatteriesBySupplierId(supplier_id)

#################### Generator Routes ####################

@app.route('/DRL/resources/generator',methods = ['GET','POST'])
def getAllGenerators():
    if request.method == 'POST':
        return GeneratorHandler().insertGenerator(request.json)
    else :
        if not request.args:
            return GeneratorHandler().getAllGenerators()
        else:
            return GeneratorHandler().searchGenerators(request.args)

@app.route('/DRL/resources/generator/<int:generator_id>', methods = ['GET','PUT','DELETE'])
def getGeneratorById(generator_id):
    if request.method == 'GET':
        return GeneratorHandler().getGeneratorById(generator_id)
    elif request.method == 'PUT':
        return GeneratorHandler().updateGenerator(generator_id, request.json)
    elif request.method == 'DELETE':
        return GeneratorHandler().deleteGenerator(generator_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/generator/supplier/<int:supplier_id>', methods = ['GET'])
def getGeneratorsBySupplierId(supplier_id):
    return GeneratorHandler().getGeneratorsBySupplierId(supplier_id)

@app.route('/DRL/resources/generator/<int:generator_id>/address', methods = ['GET'])
def getGeneratorAddress(generator_id):
    return GeneratorHandler().getGeneratorAddress(generator_id)

@app.route('/DRL/resources/generator/available',methods = ['GET'])
def getAllAvailableGenerators():
    return GeneratorHandler().getAllAvailableGenerators()

@app.route('/DRL/resources/generator/available/supplier/<int:supplier_id>',methods = ['GET'])
def getAllAvailableGeneratorsBySupplierId(supplier_id):
    return GeneratorHandler().getAllAvailableGeneratorsBySupplierId(supplier_id)

@app.route('/DRL/resources/generator/reserved',methods = ['GET'])
def getAllReservedGenerators():
    return GeneratorHandler().getAllReservedGenerators()

@app.route('/DRL/resources/generator/reserved/supplier/<int:supplier_id>',methods = ['GET'])
def getAllReservedGeneratorsBySupplierId(supplier_id):
    return GeneratorHandler().getAllReservedGeneratorsBySupplierId(supplier_id)

#################### Water Routes ####################

@app.route("/DRL/resources/water", methods=['GET', 'POST'])
def getAllWaters():
    if request.method == 'POST':
        return WaterHandler().insertWater(request.json)
    else:
        if not request.args:
            return WaterHandler().getAllWaters()
        else:
            return WaterHandler().searchWaters(request.args)

@app.route('/DRL/resources/water/<int:water_id>', methods=['GET', 'PUT', 'DELETE'])
def getWaterById(water_id):
    if request.method == 'GET':
        return WaterHandler().getWaterById(water_id)
    elif request.method == 'PUT':
        return WaterHandler().updateWater(water_id, request.json)
    elif request.method == 'DELETE':
        return WaterHandler().deleteWater(water_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/water/supplier/<int:supplier_id>', methods = ['GET'])
def getWatersBySupplierId(supplier_id):
    return WaterHandler().getWatersBySupplierId(supplier_id)

@app.route('/DRL/resources/water/<int:water_id>/address', methods = ['GET'])
def getWaterAddress(water_id):
    return WaterHandler().getWaterAddress(water_id)

@app.route('/DRL/resources/water/available', methods = ['GET'])
def getAllAvailableWaters():
    return WaterHandler().getAllAvailableWaters()

@app.route('/DRL/resources/water/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableWatersBySupplierId(supplier_id):
    return WaterHandler().getAllAvailableWatersBySupplierId(supplier_id)

@app.route('/DRL/resources/water/reserved', methods = ['GET'])
def getAllReservedWaters():
    return WaterHandler().getAllReservedWaters()

@app.route('/DRL/resources/water/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedWatersBySupplierId(supplier_id):
    return WaterHandler().getAllReservedWatersBySupplierId(supplier_id)

#################### Cloth Routes ####################

@app.route("/DRL/resources/cloth", methods=['GET', 'POST'])
def getAllClothes():
    if request.method == 'POST':
        return ClothHandler().insertCloth(request.json)
    else:
        if not request.args:
            return ClothHandler().getAllClothes()
        else:
            return ClothHandler().searchClothes(request.args)

@app.route('/DRL/resources/cloth/<int:cloth_id>', methods=['GET', 'PUT', 'DELETE'])
def getClothById(cloth_id):
    if request.method == 'GET':
        return ClothHandler().getClothById(cloth_id)
    elif request.method == 'PUT':
        return ClothHandler().updateCloth(cloth_id, request.json)
    elif request.method == 'DELETE':
        return ClothHandler().deleteCloth(cloth_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/cloth/supplier/<int:supplier_id>', methods = ['GET'])
def getClothesBySupplierId(supplier_id):
    return ClothHandler().getClothesBySupplierId(supplier_id)

@app.route('/DRL/resources/cloth/<int:cloth_id>/address', methods = ['GET'])
def getClothAddress(cloth_id):
    return ClothHandler().getClothAddress(cloth_id)

@app.route('/DRL/resources/cloth/available', methods = ['GET'])
def getAllAvailableClothes():
    return ClothHandler().getAllAvailableClothes()

@app.route('/DRL/resources/cloth/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableClothesBySupplierId(supplier_id):
    return ClothHandler().getAllAvailableClothesBySupplierId(supplier_id)

@app.route('/DRL/resources/cloth/reserved', methods = ['GET'])
def getAllReservedClothes():
    return ClothHandler().getAllReservedClothes()

@app.route('/DRL/resources/cloth/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedClothesBySupplierId(supplier_id):
    return ClothHandler().getAllReservedClothesBySupplierId(supplier_id)

#################### Heavy Equipment Routes ####################

@app.route("/DRL/resources/heavyequipment", methods=['GET', 'POST'])
def getAllHeavyEquip():
    if request.method == 'POST':
        return HeavyEquipHandler().insertHeavyEquip(request.json)
    else:
        if not request.args:
            return HeavyEquipHandler().getAllHeavyEquip()
        else:
            return HeavyEquipHandler().searchHeavyEquip(request.args)

@app.route('/DRL/resources/heavyequipment/<int:hequip_id>', methods=['GET', 'PUT', 'DELETE'])
def getHeavyEquipById(hequip_id):
    if request.method == 'GET':
        return HeavyEquipHandler().getHeavyEquipById(hequip_id)
    elif request.method == 'PUT':
        return HeavyEquipHandler().updateHeavyEquip(hequip_id, request.json)
    elif request.method == 'DELETE':
        return HeavyEquipHandler().deleteHeavyEquip(hequip_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/heavyequipment/supplier/<int:supplier_id>', methods = ['GET'])
def getHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getHeavyEquipBySupplierId(supplier_id)

@app.route('/DRL/resources/heavyequipment/<int:hequip_id>/address', methods = ['GET'])
def getHeavyEquipAddress(hequip_id):
    return HeavyEquipHandler().getHeavyEquipAddress(hequip_id)

@app.route('/DRL/resources/heavyequipment/available', methods = ['GET'])
def getAllAvailableHeavyEquip():
    return HeavyEquipHandler().getAllAvailableHeavyEquip()

@app.route('/DRL/resources/heavyequipment/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getAllAvailableHeavyEquipBySupplierId(supplier_id)

@app.route('/DRL/resources/heavyequipment/reserved', methods = ['GET'])
def getAllReservedHeavyEquip():
    return HeavyEquipHandler().getAllReservedHeavyEquip()

@app.route('/DRL/resources/heavyequipment/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedHeavyEquipBySupplierId(supplier_id):
    return HeavyEquipHandler().getAllReservedHeavyEquipBySupplierId(supplier_id)

#################### Medical Device Routes ####################

@app.route("/DRL/resources/medicaldevice", methods=['GET', 'POST'])
def getAllMedDevices():
    if request.method == 'POST':
        return MedDeviceHandler().insertMedDevice(request.json)
    else:
        if not request.args:
            return MedDeviceHandler().getAllMedDevices()
        else:
            return MedDeviceHandler().searchMedDevices(request.args)

@app.route('/DRL/resources/medicaldevice/<int:mdevice_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedDeviceById(mdevice_id):
    if request.method == 'GET':
        return MedDeviceHandler().getMedDeviceById(mdevice_id)
    elif request.method == 'PUT':
        return MedDeviceHandler().updateMedDevice(mdevice_id, request.json)
    elif request.method == 'DELETE':
        return MedDeviceHandler().deleteMedDevice(mdevice_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DRL/resources/medicaldevice/supplier/<int:supplier_id>', methods = ['GET'])
def getMedDevicesBySupplierId(supplier_id):
    return MedDeviceHandler().getMedDevicesBySupplierId(supplier_id)

@app.route('/DRL/resources/medicaldevice/<int:mdevice_id>/address', methods = ['GET'])
def getMedDeviceAddress(mdevice_id):
    return MedDeviceHandler().getMedDeviceAddress(mdevice_id)

@app.route('/DRL/resources/medicaldevice/available', methods = ['GET'])
def getAllAvailableMedDevices():
    return MedDeviceHandler().getAllAvailableMedDevices()

@app.route('/DRL/resources/medicaldevice/available/supplier/<int:supplier_id>', methods = ['GET'])
def getAllAvailableMedDevicesBySupplierId(supplier_id):
    return MedDeviceHandler().getAllAvailableMedDevicesBySupplierId(supplier_id)

@app.route('/DRL/resources/medicaldevice/reserved', methods = ['GET'])
def getAllReservedMedDevices():
    return MedDeviceHandler().getAllReservedMedDevices()

@app.route('/DRL/resources/medicaldevice/reserved/supplier/<int:supplier_id>', methods = ['GET'])
def getAllReservedMedDevicesBySupplierId(supplier_id):
    return MedDeviceHandler().getAllReservedMedDevicesBySupplierId(supplier_id)

if __name__ == '__main__':
    app.run(debug=True)

