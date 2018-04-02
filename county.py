from database_manager import DatabaseManager


INSERT_COUNTY_TEMPLATE = "INSERT INTO county (state_id, county_name) VALUES ({0}, \"{1}\");"
DELETE_COUNTIES_TEMPLATE = "DELETE FROM county;"
SELECT_COUNTIES_TEMPLATE = "SELECT id, state_id, county_name FROM county;"


class County:
    def __init__(self, county_id, state_id, county_name):
        self.county_id = county_id
        self.state_id = state_id
        self.county_name = county_name


class CountyDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete county records
        cursor.execute(DELETE_COUNTIES_TEMPLATE)

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def __init__(self):
        self.county_data = {}

        self.update()

    def get_county(self, state_id, county_name):
        for county in self.county_data.values():
            if state_id == county.state_id and county_name == county.county_name:
                return county

        return None

    def insert_data(self, state_id, county_name):
        # check to see if county already exists
        county = self.get_county(state_id, county_name)
        if county is not None:
            return county

        # insert new county data
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(INSERT_COUNTY_TEMPLATE.format(state_id, county_name))
        county_id = cursor.lastrowid

        # create County object
        county = County(county_id, state_id, county_name)

        # update county_data dictionary; there should only be one record
        # created per county
        self.county_data[county_id] = county

        # commit changes
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

        # return new county
        return county

    def update(self):
        # clear county dictionary
        self.county_data.clear()

        # retrieve county records from database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(SELECT_COUNTIES_TEMPLATE)

        # create County objects from records
        for (id, state_id, county_name) in cursor:
            self.county_data[int(id)] = County(int(id), int(state_id), county_name)

        # close connection and cursor
        cursor.close()
        db_conn.close()
