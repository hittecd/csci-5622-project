from database_manager import DatabaseManager


INSERT_METRO_TEMPLATE = "INSERT INTO metro (state_id, metro_name) VALUES ({0}, \"{1}\");"
DELETE_METROS_TEMPLATE = "DELETE FROM metro;"
SELECT_METROS_TEMPLATE = "SELECT id, state_id, metro_name FROM metro;"


class Metro:
    def __init__(self, metro_id, state_id, metro_name):
        self.metro_id = metro_id
        self.state_id = state_id
        self.metro_name = metro_name


class MetroDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete metro records
        cursor.execute(DELETE_METROS_TEMPLATE)

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def __init__(self):
        self.metro_data = {}

        self.update()

    def get_metro(self, state_id, metro_name):
        for metro in self.metro_data.values():
            if state_id == metro.state_id and metro_name == metro.metro_name:
                return metro

        return None

    def insert_data(self, state_id, metro_name):
        # check to see if metro already exists
        metro = self.get_metro(state_id, metro_name)
        if metro is not None:
            return metro

        # insert new metro data
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(INSERT_METRO_TEMPLATE.format(state_id, metro_name))
        metro_id = cursor.lastrowid

        # create Metro object
        metro = Metro(metro_id, state_id, metro_name)

        # update metro_data dictionary; there should only be one record
        # created per metro
        self.metro_data[metro_id] = metro

        # commit changes
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

        # return new metro
        return metro

    def update(self):
        # clear metro dictionary
        self.metro_data.clear()

        # retrieve metro records from database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(SELECT_METROS_TEMPLATE)

        # create Metro objects from records
        for (id, state_id, metro_name) in cursor:
            self.metro_data[int(id)] = Metro(int(id), int(state_id), metro_name)

        # close connection and cursor
        cursor.close()
        db_conn.close()
