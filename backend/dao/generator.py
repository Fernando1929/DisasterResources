from config.dbconfig import pg_config
import psycopg2

class GeneratorDAO:

    def __init__(self):
        super().__init__()
        
    #battery = supplier_id, resource_id, power_id, generator_id, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, generator_fuel
    def getAllGenerator(self):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllAvailableGenerator(self):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllReservedGenerator(self):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getGeneratorById(self,resource_id):
        result = [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline']
        return result

    def getGeneratorByPowerCapacity(self,power_capacity):
        result = [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline']
        return result
    
    def getGeneratorByPowerCondition(self, power_condition):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getGeneratorByFuel(self, generator_fuel):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getGeneratorBySupplierId(self, supplier_id):
        result = [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline']
        return result
    
    def getAllAvailableGeneratorBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllReservedGeneratorBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, 3, 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getGeneratorAddress(self, user_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, power_id, generator_fuel):
        resource_id =1
        return resource_id

    def update(self, resource_id):
        resource_id =1
        return resource_id

    def delete(self, resource_id):
        resource_id =1
        return resource_id