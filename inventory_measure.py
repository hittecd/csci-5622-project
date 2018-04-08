from datetime import date

from database_manager import DatabaseManager


INVENTORY_MEASURE_TABLE = "inventory_measure"
INVENTORY_MEASURE_SSA_TABLE = "inventory_measure_ssa"

state_abbr = {"Alabama": "AK",
              "Alaska": "AL",
              "Arizona": "AL",
              "Arkansas": "AR",
              "California": "CA",
              "Colorado": "CO",
              "Connecticut": "CT",
              "Delaware": "DE",
              "District of Columbia": "DC",
              "Florida": "FL",
              "Georgia": "GA",
              "Hawaii": "HI",
              "Idaho": "ID",
              "Illinois": "IL",
              "Indiana": "IN",
              "Iowa": "IA",
              "Kansas": "KA",
              "Kentucky": "KY",
              "Louisiana": "LA",
              "Maine": "ME",
              "Maryland": "MD",
              "Massachusetts": "MA",
              "Michigan": "MI",
              "Minnesota": "MN",
              "Mississippi": "MS",
              "Missouri": "MO",
              "Montana": "MT",
              "Nebraska": "NE",
              "Nevada": "NV",
              "New Hampshire": "NH",
              "New Jersey": "NJ",
              "New Mexico": "NM",
              "New York": "NY",
              "North Carolina": "NC",
              "North Dakota": "ND",
              "Ohio": "OH",
              "Oklahoma": "OK",
              "Oregon": "OR",
              "Pennsylvania": "PA",
              "Rhode Island": "RI",
              "South Carolina": "SC",
              "South Dakota": "SD",
              "Tennessee": "TN",
              "Texas": "TX",
              "Utah": "UT",
              "Vermont": "VT",
              "Virginia": "VA",
              "Washington": "WA",
              "West Virginia": "WV",
              "Wisconsin": "WI",
              "Wyoming": "WY"}

ZIP_INDEX = 0
CITY_INDEX = 2
COUNTY_NAME_INDEX = 3
METRO_INDEX = 4
STATE_INDEX = 5
INVENTORY_MEASURE_DATA_MIN_INDEX = 7

INSERT_INVENTORY_MEASURE_TEMPLATE = "INSERT INTO {0} (zip_id, date_time, inventory) VALUES ({1}, \"{2}\", {3});"
DELETE_INVENTORY_MEASURE_TEMPLATE = "DELETE FROM {0};"


class InventorMeasureDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete median listing price records across all tables
        cursor.execute(DELETE_INVENTORY_MEASURE_TEMPLATE.format(INVENTORY_MEASURE_TABLE))
        cursor.execute(DELETE_INVENTORY_MEASURE_TEMPLATE.format(INVENTORY_MEASURE_SSA_TABLE))

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

    def insert_inventory_measure_data(self, table, data_file):
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # parse data lines
        data_lines = data_file.readlines()

        date_fields = data_lines[0].replace('\"', '').split(',')[INVENTORY_MEASURE_DATA_MIN_INDEX:]

        for data_line in data_lines[1:]:
            # split data line
            data_line = data_line.replace('\"', '').split(',')

            # get record fields from data line
            zip_data = data_line[ZIP_INDEX]
            state_data = state_abbr[data_line[STATE_INDEX]]
            county_data = data_line[COUNTY_NAME_INDEX]
            metro_data = data_line[METRO_INDEX]
            city_data = data_line[CITY_INDEX]
            inventory_measure_data = \
                data_line[INVENTORY_MEASURE_DATA_MIN_INDEX:]

            # get parent record objects
            state = self.state_dao.insert_data(state_data)
            county = self.county_dao.insert_data(state.state_id, county_data)
            metro = self.metro_dao.insert_data(state.state_id, metro_data)
            city = self.city_dao.insert_data(county.county_id, metro.metro_id, state.state_id, city_data)
            zip_code = self.zip_dao.insert_data(city.city_id, county.county_id, metro.metro_id, state.state_id, zip_data)

            # insert median listing price records
            for date_time, inventory_measure in zip(date_fields, inventory_measure_data):
                # format date
                date_time = date_time.split('-')
                date_time = date(int(date_time[0]), int(date_time[1]), 1)  # MM/1/YYYY

                # format median listing price
                if inventory_measure == '':
                    inventory_measure = "NULL"
                else:
                    inventory_measure = int(inventory_measure)

                cursor.execute(INSERT_INVENTORY_MEASURE_TEMPLATE.format(table, zip_code.zip_id, date_time.isoformat(), inventory_measure))

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def insert_inventory_measure_all_homes_data(self):
        data_file = open("data/InventoryMeasure_Zip_Public.csv", "r")

        self.insert_inventory_measure_data(INVENTORY_MEASURE_TABLE, data_file)

    def insert_inventory_measure_condo_data(self):
        data_file = open("data/InventoryMeasure_SSA_Zip_Public.csv", "r")

        self.insert_inventory_measure_data(INVENTORY_MEASURE_SSA_TABLE, data_file)

    def insert_data(self):
        # insert inventory measure data
        self.insert_inventory_measure_all_homes_data()

        self.insert_inventory_measure_condo_data()
