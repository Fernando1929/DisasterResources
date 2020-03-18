from flask import jsonify
from dao.resource import ResourceDAO
from dao.medicine import MedicineDAO

class MedicineHandler:
    def build_medicine_dict(self, row):
        result = {}
        result['med_id'] = row[0]
        result['resource_id'] = row[1]
        result['supplier_id'] = row[2]
        result['med_name'] = row[3]
        result['med_brand'] = row[4]
        result['med_quantity'] = row[5]
        result['med_price'] = row[6]
        result['med_type'] = row[7]
        result['med_dose'] = row[8]
        result['med_prescript'] = row[9]
        result['med_expdate'] = row[10]
        return result

    def build_medicine_attributes(self, med_id, resource_id, supplier_id, med_name, med_brand, med_quantity, med_price, med_type, med_dose, med_prescript, med_expdate):
        result = {}
        result['med_id'] = med_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['med_name'] = med_name
        result['med_brand'] = med_brand
        result['med_quantity'] = med_quantity
        result['med_price'] = med_price
        result['med_type'] = med_type
        result['med_dose'] = med_dose
        result['med_prescript'] = med_prescript
        result['med_expdate'] = med_expdate
        return result

    def getAllMedicines(self):
        dao = MedicineDAO()
        med_list = dao.getAllMedicines()
        result_list = []
        for row in med_list:
            result = self.build_medicine_dict(row)
            result_list.append(result)
        return jsonify(Medicines = result_list)

    def getMedicineById(self, med_id):
        dao = MedicineDAO()
        row = dao.getMedicineById(med_id)
        if not row:
            return jsonify(Error = "Medicine Not Found"), 404
        else:
            medicine = self.build_medicine_dict(row)
            return jsonify(Medicine = medicine)

    def getMedicineBySupplierId(self, supplier_id):
        med_list = []
        result_list = []
        med_dao = MedicineDAO()
        med_list = med_dao.getMedicinesBySupplierId(supplier_id)
        for row in med_list:
            result = self.build_medicine_dict(row)
            result_list.append(result)
        return jsonify(Medicine = result_list)

    def searchMedicine(self, args):
        med_brand = args.get("med_brand")
        med_type = args.get("med_type")
        med_dose = args.get("med_dose")
        med_prescript = args.get("med_prescript")
        med_expdate = args.get("med_expdate")

        dao = MedicineDAO()
        med_list = []
        if (len(args) == 1) and med_brand:
            med_list = dao.getMedicineByBrand(med_brand)
        elif (len(args) == 1) and med_type:
            med_list = dao.getMedicinesByType(med_type)
        elif (len(args) == 1) and med_prescript:
            med_list = dao.getMedicinesByPrescription(med_prescript)
        elif (len(args) == 2) and med_type and med_dose:
            med_list = dao.getMedicinesByTypeAndDose(med_type, med_dose)
        elif (len(args) == 2) and med_type and med_prescript:
            med_list = dao.getMedicinesByTypeAndPrescription(med_type, med_prescript)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in med_list:
            result = self.build_medicine_dict(row)
            result_list.append(result)
        return jsonify(Medicine = result_list)

    def insertMedicine(self, json):
        supplier_id = json["supplier_id"]
        med_name = json["med_name"]
        med_brand = json["med_brand"]
        med_quantity = json["med_quantity"]
        med_price = json["med_price"]
        med_type = json["med_type"]
        med_dose = json["med_dose"]
        med_prescript = json["med_prescript"]
        med_expdate = json["med_expdate"]

        if supplier_id and med_name and med_brand and med_quantity and med_price and med_type and med_dose and med_prescript and med_expdate:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, med_name, med_brand, med_quantity, med_price)
            med_dao = MedicineDAO()
            med_id = med_dao.insert(resource_id, med_type, med_dose, med_prescript, med_expdate)
            result = self.build_medicine_attributes(med_id, resource_id, supplier_id, med_name, med_brand, med_quantity, med_price, med_type, med_dose, med_prescript, med_expdate)
            return jsonify(Medicine = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateMedicine(self, med_id, json):
        med_dao = MedicineDAO()
        if not med_dao.getMedicineById(med_id):
            return jsonify(Error = "Medicine not found."), 404
        else:
            supplier_id = json["supplier_id"]
            med_name = json["med_name"]
            med_brand = json["med_brand"]
            med_quantity = json["med_quantity"]
            med_price = json["med_price"]
            med_type = json["med_type"]
            med_dose = json["med_dose"]
            med_prescript = json["med_prescript"]
            med_expdate = json["med_expdate"]

            if supplier_id and med_name and med_brand and med_quantity and med_price and med_type and med_dose and med_prescript and med_expdate:
                resource_id = med_dao.update(med_id, med_type, med_dose, med_prescript, med_expdate)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, med_name, med_brand, med_quantity, med_price)
             
                result = self.build_medicine_attributes(med_id, resource_id, supplier_id, med_name, med_brand, med_quantity, med_price, med_type, med_dose, med_prescript, med_expdate)
                return jsonify(Medicine = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteMedicine(self, med_id):
        med_dao = MedicineDAO()
        if not med_dao.getMedicineById(med_id):
            return jsonify(Error = "Medicine not found."), 404
        else:
            resource_id = med_dao.delete(med_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200