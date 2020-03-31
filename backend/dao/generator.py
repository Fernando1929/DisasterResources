from config.dbconfig import pg_config
import psycopg2

class GeneratorDAO:

    def __init__(self):
        super().__init__()
        
    # generator = supplier_id, resource_id, power_id, generator_id, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, generator_fuel
    
    def getAllGenerators(self):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllAvailableGenerators(self):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllReservedGenerators(self):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getAllRequestedGenerators(self):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getGeneratorById(self, generator_id):
        result = [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline']
        return result

    def getGeneratorsByPowerCapacity(self,power_capacity):
        result = [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline']
        return result
    
    def getGeneratorsByPowerCondition(self, power_condition):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getGeneratorsByFuel(self, generator_fuel):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getGeneratorsBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getGeneratorsByResourceId(self, resource_id):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllAvailableGeneratorsBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result
    
    def getAllReservedGeneratorsBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
        ]
        return result

    def getAllRequestedGeneratorsBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, 3, "generator", 'generator', 'WEN', 10, 300.00, 1.20, 'new', 'gasoline'],
            [2, 1, 2, 4, "generator", 'generator', 'CAT', 8, 500.00, 40, 'new', 'diesel']
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