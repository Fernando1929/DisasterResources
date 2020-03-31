class MedicineDAO:
    def __init__(self):
        super().__init__()

# medicine = med_id, resource_id, category, supplier_id, med_name, med_brand, med_quantity, med_price, 
#           med_type, med_dose, med_prescript, med_expdate

    def getAllMedicines(self):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllAvailableMedicines(self):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllReservedMedicines(self):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllRequestedMedicines(self):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicineById(self, med_id):
        result = [1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]
        return result

    def getMedicineByResourceId(self, resource_id):
        result = [1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]
        return result

    def getMedicinesByBrand(self, resource_brand):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByType(self, med_type):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByPrescription(self, med_prescript):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByTypeAndDose(self, med_type, med_dose):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByTypeAndPrescription(self, med_type, med_prescript):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllAvailableMedicinesBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllReservedMedicinesBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "medicine", "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllRequestedMedicinesBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "medicine", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicineAddress(self, supplier_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, med_type, med_dose, med_prescript, med_expdate):
        med_id = 1
        return med_id

    def delete(self, med_id):
        resource_id = 1
        return resource_id

    def update(self, med_id, med_type, med_dose, med_prescript, med_expdate):
        resource_id = 1
        return resource_id
