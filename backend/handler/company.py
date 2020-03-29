from flask import jsonify
from dao.company import CompanyDAO 

class CompanyHandler:

    #company = company_id, company_name, company_address, company_phone
    def build_company_dict(self, row):
        result = {}
        result['company_id'] = row[0]
        result['company_name'] = row[1]
        result['company_address'] = row[2]
        result['company_phone'] = row[3]
        return result

    def build_company_attributes(self, company_id, company_name, company_address, company_phone):
        result = {}
        result['company_id'] = company_id
        result['company_name'] = company_name
        result['company_address'] = company_address 
        result['company_phone'] = company_phone
        return result

    def getAllCompanies(self):
        dao = CompanyDAO()
        result = dao.getAllCompanies()
        result_list = []
        for row in result:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Companies=result_list)

    def getCompanyById(self, company_id):
        dao = CompanyDAO()
        row = dao.getCompanyById(company_id)
        if not row:
            return jsonify(Error = "Company Not Found"), 404
        else:
            order = self.build_company_dict(row)
            return jsonify(Company = order)

    def getCompanyBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
            company_dao = CompanyDAO()
            result_list = []
            company_list = company_dao.getCompanyBySupplierId(supplier_id)
            for row in company_list:
                result = self.build_company_dict(row)
                result_list.append(result)
            return jsonify(Company=result_list)

    def searchCompany(self, args):
        company_name = args['company_name']
        company_address = args['company_address']
        company_phone = args['company_phone']
        dao = CompanyDAO()
        companies_list = []
        if (len(args) == 1) and company_name:
            companies_list = dao.getCompanyByName(company_name)
        elif (len(args) == 1) and company_address:
            companies_list = dao.getCompanyByAddress(company_address)
        elif (len(args) == 1) and company_phone:
            companies_list = dao.getCompanyByPhone(company_phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in companies_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Companies=result_list)

    def insertCompany(self, json):
        company_name = json['company_name']
        company_address = json['company_address']
        company_phone = json['company_phone']
        if company_name and company_address and company_phone:
            dao = CompanyDAO()
            company_id = dao.insert(company_name, company_address, company_phone)
            json = self.build_company_attributes(company_id, company_name, company_address, company_phone)
            return jsonify(Company=json), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteCompany(self, company_id):
        dao = CompanyDAO()
        if not dao.getCompanyById(company_id):
            return jsonify(Error = "Company not found."), 404
        else:
            dao.delete(company_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateCompany(self, company_id, json):
        dao = CompanyDAO()
        if not dao.getCompanyById(company_id):
            return jsonify(Error = "Company not found."), 404
        else:
            company_id = json['company_id']
            company_name = json['company_name']
            company_address = json['company_address']
            company_phone = json['company_phone']
            if company_id and company_name and company_address and company_phone:
                dao.update(company_id, company_name, company_address, company_phone)
                result = self.build_company_attributes(company_id, company_name, company_address, company_phone)
                return jsonify(Company=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400
