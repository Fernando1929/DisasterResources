class FuelDAO:
    def __init__(self):
        super().__init__()

# fuel = fuel_id, resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price, 
#           fuel_type, fuel_gallons
    def getAllFuels(self):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllAvailableFuel(self):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllReservedFuel(self):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllRequestedFuel(self):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelById(self, fuel_id):
        result = [1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]
        return result

    def getFuelByResourceId(self, resource_id):
        result = [1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]
        return result

    def getFuelByBrand(self, resource_brand):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsByType(self, fuel_type):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsByGallons(self, fuel_gallons):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsByTypeAndGallons(self, fuel_type, fuel_gallons):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllAvailableFuelBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllReservedFuelBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllRequestedFuelBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelAddress(self, supplier_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, fuel_type, fuel_gallons):
        fuel_id = 1
        return fuel_id

    def delete(self, fuel_id):
        resource_id = 1
        return resource_id

    def update(self, fuel_id, fuel_type, fuel_gallons):
        resource_id = 1
        return resource_id