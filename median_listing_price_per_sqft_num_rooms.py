from datetime import date

from database_manager import DatabaseManager


MEDIAN_LISTING_PRICE_PER_SQFT_ONE_ROOM_TABLE = "median_listing_price_per_sqft_one_room"
MEDIAN_LISTING_PRICE_PER_SQFT_TWO_ROOM_TABLE = "median_listing_price_per_sqft_two_room"
MEDIAN_LISTING_PRICE_PER_SQFT_THREE_ROOM_TABLE = "median_listing_price_per_sqft_three_room"
MEDIAN_LISTING_PRICE_PER_SQFT_FOUR_ROOM_TABLE = "median_listing_price_per_sqft_four_room"
MEDIAN_LISTING_PRICE_PER_SQFT_FIVE_PLUS_ROOM_TABLE = "median_listing_price_per_sqft_five_plus_room"

ZIP_INDEX = 0
CITY_INDEX = 1
STATE_INDEX = 2
METRO_INDEX = 3
COUNTY_NAME_INDEX = 4
SIZE_RANK_INDEX = 5
MEDIAN_LISTING_PRICE_DATA_MIN_INDEX = 6

INSERT_MEDIAN_LISTING_PRICE_TEMPLATE = "INSERT INTO {0} (zip_id, date_time, price) VALUES ({1}, \"{2}\", {3});"
DELETE_MEDIAN_LISTING_PRICE_TEMPLATE = "DELETE FROM {0};"


class MedianListingPricePerSqftNumBedroomsDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete median listing price records across all tables
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_PER_SQFT_ONE_ROOM_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_PER_SQFT_TWO_ROOM_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_PER_SQFT_THREE_ROOM_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_PER_SQFT_FOUR_ROOM_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_PER_SQFT_FIVE_PLUS_ROOM_TABLE))

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

    def insert_median_listing_price_per_sqft_data(self, table, data_file):
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # parse data lines
        data_lines = data_file.readlines()

        date_fields = data_lines[0].replace('\"', '').split(',')[MEDIAN_LISTING_PRICE_DATA_MIN_INDEX:]

        for data_line in data_lines[1:]:
            # split data line
            data_line = data_line.replace('\"', '').split(',')

            # get record fields from data line
            zip_data = int(data_line[ZIP_INDEX])
            state_data = data_line[STATE_INDEX]
            county_data = data_line[COUNTY_NAME_INDEX]
            metro_data = data_line[METRO_INDEX]
            city_data = data_line[CITY_INDEX]
            median_listing_price_data = \
                data_line[MEDIAN_LISTING_PRICE_DATA_MIN_INDEX:]

            # get parent record objects
            state = self.state_dao.insert_data(state_data)
            county = self.county_dao.insert_data(state.state_id, county_data)
            metro = self.metro_dao.insert_data(state.state_id, metro_data)
            city = self.city_dao.insert_data(county.county_id, metro.metro_id, state.state_id, city_data)
            zip_code = self.zip_dao.insert_data(city.city_id, county.county_id, metro.metro_id, state.state_id, zip_data)

            # insert median listing price records
            for date_time, median_listing_price in zip(date_fields, median_listing_price_data):
                # format date
                date_time = date_time.split('-')
                date_time = date(int(date_time[0]), int(date_time[1]), 1)  # MM/1/YYYY

                # format median listing price
                if median_listing_price == '':
                    median_listing_price = "NULL"
                else:
                    median_listing_price = float(median_listing_price)

                cursor.execute(INSERT_MEDIAN_LISTING_PRICE_TEMPLATE.format(table, zip_code.zip_id, date_time.isoformat(), median_listing_price))

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def insert_median_listing_price_per_sqft_one_room_data(self):
        data_file = open("data/Zip_MedianListingPricePerSqft_1Bedroom.csv", "r")

        self.insert_median_listing_price_per_sqft_data(MEDIAN_LISTING_PRICE_PER_SQFT_ONE_ROOM_TABLE, data_file)

    def insert_median_listing_price_per_sqft_two_room_data(self):
        data_file = open("data/Zip_MedianListingPricePerSqft_2Bedroom.csv", "r")

        self.insert_median_listing_price_per_sqft_data(MEDIAN_LISTING_PRICE_PER_SQFT_TWO_ROOM_TABLE, data_file)

    def insert_median_listing_price_per_sqft_three_room_data(self):
        data_file = open("data/Zip_MedianListingPricePerSqft_3Bedroom.csv", "r")

        self.insert_median_listing_price_per_sqft_data(MEDIAN_LISTING_PRICE_PER_SQFT_THREE_ROOM_TABLE, data_file)

    def insert_median_listing_price_per_sqft_four_room_data(self):
        data_file = open("data/Zip_MedianListingPricePerSqft_4Bedroom.csv", "r")

        self.insert_median_listing_price_per_sqft_data(MEDIAN_LISTING_PRICE_PER_SQFT_FOUR_ROOM_TABLE, data_file)

    def insert_median_listing_price_per_sqft_five_plus_room_data(self):
        data_file = open("data/Zip_MedianListingPricePerSqft_5BedroomOrMore.csv", "r")

        self.insert_median_listing_price_per_sqft_data(MEDIAN_LISTING_PRICE_PER_SQFT_FIVE_PLUS_ROOM_TABLE, data_file)

    def insert_data(self):
        # insert median listing price data
        self.insert_median_listing_price_per_sqft_one_room_data()

        self.insert_median_listing_price_per_sqft_two_room_data()

        self.insert_median_listing_price_per_sqft_three_room_data()

        self.insert_median_listing_price_per_sqft_four_room_data()

        self.insert_median_listing_price_per_sqft_five_plus_room_data()
