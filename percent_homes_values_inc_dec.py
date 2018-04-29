from datetime import date

from database_manager import DatabaseManager


PERCENT_HOMES_VALUES_INCREASING_TABLE = "percent_homes_values_increasing"
PERCENT_HOMES_VALUES_DECREASING_TABLE = "percent_homes_values_decreasing"

ZIP_INDEX = 1
CITY_INDEX = 2
STATE_INDEX = 3
METRO_INDEX = 4
COUNTY_NAME_INDEX = 5
SIZE_RANK_INDEX = 6
PERCENT_HOMES_VALUES_DATA_MIN_INDEX = 7

INSERT_PERCENT_HOMES_VALUES_TEMPLATE = "INSERT INTO {0} (zip_id, date_time, percent) VALUES ({1}, \"{2}\", {3});"
DELETE_PERCENT_HOMES_VALUES_TEMPLATE = "DELETE FROM {0};"


class PercentHomesValuesIncDecDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete percent homes values records across all tables
        cursor.execute(DELETE_PERCENT_HOMES_VALUES_TEMPLATE.format(PERCENT_HOMES_VALUES_INCREASING_TABLE))
        cursor.execute(DELETE_PERCENT_HOMES_VALUES_TEMPLATE.format(PERCENT_HOMES_VALUES_DECREASING_TABLE))

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def __init__(self, state_dao, county_dao, metro_dao, city_dao, zip_dao):
        self.state_dao = state_dao
        self.county_dao = county_dao
        self.metro_dao = metro_dao
        self.city_dao = city_dao
        self.zip_dao = zip_dao

    def insert_percent_homes_values_data(self, table, data_file):
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # parse data lines
        data_lines = data_file.readlines()

        date_fields = data_lines[0].replace('\"', '').split(',')[PERCENT_HOMES_VALUES_DATA_MIN_INDEX:]

        for data_line in data_lines[1:]:
            # split data line
            data_line = data_line.replace('\"', '').split(',')

            # get record fields from data line
            zip_data = data_line[ZIP_INDEX]
            state_data = data_line[STATE_INDEX]
            county_data = data_line[COUNTY_NAME_INDEX]
            metro_data = data_line[METRO_INDEX]
            city_data = data_line[CITY_INDEX]
            percent_home_value_data = \
                data_line[PERCENT_HOMES_VALUES_DATA_MIN_INDEX:]

            # get parent record objects
            state = self.state_dao.insert_data(state_data)
            county = self.county_dao.insert_data(state.state_id, county_data)
            metro = self.metro_dao.insert_data(state.state_id, metro_data)
            city = self.city_dao.insert_data(county.county_id, metro.metro_id, state.state_id, city_data)
            zip_code = self.zip_dao.insert_data(city.city_id, county.county_id, metro.metro_id, state.state_id, zip_data)

            # insert percent homes values records
            for date_time, percent_home_value in zip(date_fields, percent_home_value_data):
                # format date
                date_time = date_time.split('-')
                date_time = date(int(date_time[0]), int(date_time[1]), 1)  # MM/1/YYYY

                # format percent homes values
                if percent_home_value == '':
                    percent_home_value = "NULL"
                else:
                    try:
                        percent_home_value = float(percent_home_value)
                    except:
                        continue

                cursor.execute(INSERT_PERCENT_HOMES_VALUES_TEMPLATE.format(table, zip_code.zip_id, date_time.isoformat(), percent_home_value))

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def insert_percent_homes_values_increasing_data(self):
        data_file = open("data/zillow/Zip_PctOfHomesIncreasingInValues_AllHomes.csv", "r")

        self.insert_percent_homes_values_data(PERCENT_HOMES_VALUES_INCREASING_TABLE, data_file)

    def insert_percent_homes_values_decreasing_data(self):
        data_file = open("data/zillow/Zip_PctOfHomesDecreasingInValues_AllHomes.csv", "r")

        self.insert_percent_homes_values_data(PERCENT_HOMES_VALUES_DECREASING_TABLE, data_file)

    def insert_data(self):
        # insert percent homes values data
        self.insert_percent_homes_values_increasing_data()

        self.insert_percent_homes_values_decreasing_data()
