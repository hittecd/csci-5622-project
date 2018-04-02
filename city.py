from database_manager import DatabaseManager


INSERT_CITY_TEMPLATE = "INSERT INTO city (county_id, metro_id, state_id, city_name) VALUES ({0}, {1}, {2}, \"{3}\");"
DELETE_CITIES_TEMPLATE = "DELETE FROM city;"
SELECT_CITIES_TEMPLATE = "SELECT id, county_id, metro_id, state_id, city_name FROM city;"


class City:
    def __init__(self, city_id, county_id, metro_id, state_id, city_name):
        self.city_id = city_id
        self.county_id = county_id
        self.metro_id = metro_id
        self.state_id = state_id
        self.city_name = city_name


class CityDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete city records
        cursor.execute(DELETE_CITIES_TEMPLATE)

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def __init__(self):
        self.city_data = {}

        self.update()

    def get_city(self, state_id, city_name):
        for city in self.city_data.values():
            if state_id == city.state_id and city_name == city.city_name:
                return city

        return None

    def insert_data(self, county_id, metro_id, state_id, city_name):
        # check to see if city already exists
        city = self.get_city(state_id, city_name)
        if city is not None:
            return city

        # insert new city data
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(INSERT_CITY_TEMPLATE.format(county_id, metro_id, state_id, city_name))
        city_id = cursor.lastrowid

        # create City object
        city = City(city_id, county_id, metro_id, state_id, city_name)

        # update city_data dictionary; there should only be one record
        # created per city
        self.city_data[city_id] = city

        # commit changes
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

        # return new city
        return city

    def update(self):
        # clear city dictionary
        self.city_data.clear()

        # retrieve city records from database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(SELECT_CITIES_TEMPLATE)

        # create City objects from records
        for (id, county_id, metro_id, state_id, city_name) in cursor:
            self.city_data[int(id)] = City(int(id), int(county_id), int(metro_id), int(state_id), city_name)

        # close connection and cursor
        cursor.close()
        db_conn.close()
