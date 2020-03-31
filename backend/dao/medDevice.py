class MedDeviceDAO:
    def __init__(self):
        super().__init__()

    # med_device = mdevice_id, resource_id, supplier_id, category, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price, mdevice_type, mdevice_model, mdevice_condition, mdevice_power

    def getAllMedDevices(self):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getAllAvailableMedDevices(self):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getAllReservedMedDevices(self):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 0.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 0.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getAllRequestedMedDevices(self):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 0.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 0.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDeviceById(self, mdevice_id):
        result = [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00, "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"]
        return result

    def getMedDeviceByResourceId(self, resource_id):
        result = [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00, "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"]
        return result

    def getMedDevicesByBrand(self, resource_brand):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDevicesByCondition(self, med_device_condition):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDevicesByType(self, med_device_type):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDevicesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 2, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getAllAvailableMedDevicesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 1900.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 1, "medical_device", "Medical Device", "Arm Style", 2, 20.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getAllReservedMedDevicesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 0.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 1, "medical_device", "Medical Device", "Arm Style", 2, 0.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getAllRequestedMedDevicesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "medical_device", "Medical Device", "Forcemech", 1, 0.00 , "Electric Wheelchair", "Voyager R2", "New", "Lithium battery"],
            [2, 2, 1, "medical_device", "Medical Device", "Arm Style", 2, 0.00, "Blood Preassure Monitor", "Annsky", "Very good", "AA batteries"]
        ]
        return result

    def getMedDeviceAddress(self, user_id):
        result = [1, 1, "Barrio Las Palmas", "Utuado", "PR", "US", "00641"]
        return result

    def insert(self, resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        mdevice_id = 1
        return mdevice_id

    def update(self, mdevice_id, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        resource_id = 1
        return resource_id

    def delete(self, mdevice_id):
        resource_id = 1
        return resource_id