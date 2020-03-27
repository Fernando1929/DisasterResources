class MedicineDAO:
    def __init__(self):
        super().__init__()


# medicine = med_id, resource_id, supplier_id, med_address, med_name, med_brand, med_quantity, med_price, 
#           med_type, med_dose, med_prescript, med_expdate
    def getAllMedicines(self):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllAvailableMedicine(self):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllReservedMedicine(self):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicineById(self, resource_id):
        result = [1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]
        return result

    def getMedicineByBrand(self, resource_brand):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByType(self, med_type):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByPrescription(self, med_prescript):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByTypeAndDose(self, med_type, med_dose):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesByTypeAndPrescription(self, med_type, med_prescript):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getMedicinesBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllAvailableMedicineBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
        return result

    def getAllReservedMedicineBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Plaza Fernando Pacheco, Yauco, PR", "Sumatriptan", "Walgreens", 1, 10.00, "migraine", "50mg", "Y", "12/31/2020"]]
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
