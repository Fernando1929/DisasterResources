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

    def update(self, id, reservation_id, resource_id, reservation_quantity):
        return id

    def delete(self, id):
        return id