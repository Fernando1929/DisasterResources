class MedDeviceDAO:
    def __init__(self):
        super().__init__()

# water = resource_id, supplier_id, resource_name, resource_brand, resource_quantity, resource_price, device_type, device_model, device_condition, device_power_type
    def getAllMedDevice(self):
        result = [
            ["1", "1", "Medical Device", "Forcemech", "1", "1900.00", "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            ["2", "2", "Medical Device", "Arm Style", "2", "20.00", "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDeviceById(self, resource_id):
        result = ["1", "1", "Medical Device", "Forcemech", "1", "1900.00", "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"]
        return result

    def getMedDeviceByBrand(self, resource_brand):
        result = [
            ["1", "1", "Medical Device", "Forcemech", "1", "1900.00", "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            ["2", "2", "Medical Device", "Arm Style", "2", "20.00", "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDeviceByCondition(self, med_device_condition):
        result = [
            ["1", "1", "Medical Device", "Forcemech", "1", "1900.00", "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            ["2", "2", "Medical Device", "Arm Style", "2", "20.00", "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDeviceByType(self, med_device_type):
        result = [
            ["1", "1", "Medical Device", "Forcemech", "1", "1900.00", "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            ["2", "2", "Medical Device", "Arm Style", "2", "20.00", "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDeviceBySupplierId(self, supplier_id):
        result = [
            ["1", "1", "Medical Device", "Forcemech", "1", "1900.00", "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            ["2", "2", "Medical Device", "Arm Style", "2", "20.00", "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def insert(self, resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        return resource_id

    def update(self, resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        return resource_id

    def delete(self, resource_id):
        return resource_id