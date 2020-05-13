from config.dbconfig import pg_config
import psycopg2

class ResourceReservationDAO:
    
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    #resource_reservation = id, reservation id, resource id, reservation quantity

    def insert(self, reservation_id, resource_id, quantity):
        cursor = self.conn.cursor()
        query = "INSERT INTO resource_reservations (reservation_id, resource_id, reservation_quantity) VALUES (%s, %s, %s);"
        cursor.execute(query, (reservation_id, resource_id, quantity,))
        self.conn.commit()

    def update(self, reservation_id, resource_id, reservation_quantity):
        cursor = self.conn.cursor()
        query = "update resource_reservations set reservation_quantity = %s where reservation_id = %s and resource_id = %s;"
        cursor.execute(query, (reservation_quantity, reservation_id, resource_id,))
        self.conn.commit()

    def delete(self, reservation_id, resource_id):
        cursor = self.conn.cursor()
        query = "delete from resource_reservations where reservation_id = %s and resource_id = %s;"
        cursor.execute(query,(reservation_id, resource_id,))
        self.conn.commit()