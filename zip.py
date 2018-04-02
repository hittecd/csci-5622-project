from database_manager import DatabaseManager


INSERT_ZIP_TEMPLATE = "INSERT INTO zip (city_id, county_id, metro_id, state_id, zip_code) VALUES ({0}, {1}, {2}, {3}, {4});"
DELETE_ZIPS_TEMPLATE = "DELETE FROM zip;"
SELECT_ZIPS_TEMPLATE = "SELECT id, city_id, county_id, metro_id, state_id, zip_code FROM zip;"


class Zip:
    def __init__(self, zip_id, city_id, county_id, metro_id, state_id, zip_code):
        self.zip_id = zip_id
        self.city_id = city_id
        self.county_id = county_id
        self.metro_id = metro_id
        self.state_id = state_id
        self.zip_code = zip_code


class ZipDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete zip records
        cursor.execute(DELETE_ZIPS_TEMPLATE)

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def __init__(self):
        self.zip_data = {}

        self.update()

    def get_zip(self, city_id, county_id, metro_id, state_id, zip_code):
        for zip in self.zip_data.values():
            if city_id == zip.city_id and county_id == zip.county_id and metro_id == zip.metro_id and state_id == zip.state_id and zip_code == zip.zip_code:
                return zip

        return None

    def insert_data(self, city_id, county_id, metro_id, state_id, zip_code):
        # check to see if zip already exists
        zip = self.get_zip(city_id, county_id, metro_id, state_id, zip_code)
        if zip is not None:
            return zip

        # insert new zip data
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(INSERT_ZIP_TEMPLATE.format(city_id, county_id, metro_id, state_id, zip_code))
        zip_id = cursor.lastrowid

        # create Zip object
        zip = Zip(zip_id, city_id, county_id, metro_id, state_id, zip_code)

        # update zip_data dictionary; there should only be one record
        # created per zip
        self.zip_data[zip_id] = zip

        # commit changes
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

        # return new zip
        return zip

    def update(self):
        # clear zip dictionary
        self.zip_data.clear()

        # retrieve zip records from database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(SELECT_ZIPS_TEMPLATE)

        # create Zip objects from records
        for (id, city_id, county_id, metro_id, state_id, zip_code) in cursor:
            self.zip_data[int(id)] = Zip(int(id), int(city_id), int(county_id), int(metro_id), int(state_id), int(zip_code))

        # close connection and cursor
        cursor.close()
        db_conn.close()
