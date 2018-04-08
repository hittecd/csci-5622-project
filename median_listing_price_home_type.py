from datetime import date

from database_manager import DatabaseManager


MEDIAN_LISTING_PRICE_ALL_HOMES_TABLE = "median_listing_price_all_homes"
MEDIAN_LISTING_PRICE_CONDO_TABLE = "median_listing_price_condo"
MEDIAN_LISTING_PRICE_DUPLEX_TRIPLEX_TABLE = "median_listing_price_duplex_triplex"
MEDIAN_LISTING_PRICE_SFR_TABLE = "median_listing_price_sfr"

ZIP_INDEX = 0
CITY_INDEX = 1
STATE_INDEX = 2
METRO_INDEX = 3
COUNTY_NAME_INDEX = 4
SIZE_RANK_INDEX = 5
MEDIAN_LISTING_PRICE_DATA_MIN_INDEX = 6

INSERT_MEDIAN_LISTING_PRICE_TEMPLATE = "INSERT INTO {0} (zip_id, date_time, price) VALUES ({1}, \"{2}\", {3});"
DELETE_MEDIAN_LISTING_PRICE_TEMPLATE = "DELETE FROM {0};"


class MedianListingPriceHomeTypeDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete median listing price records across all tables
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_ALL_HOMES_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_CONDO_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_DUPLEX_TRIPLEX_TABLE))
        cursor.execute(DELETE_MEDIAN_LISTING_PRICE_TEMPLATE.format(MEDIAN_LISTING_PRICE_SFR_TABLE))

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

    def insert_median_listing_price_data(self, table, data_file):
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
            zip_data = data_line[ZIP_INDEX]
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

    def insert_median_listing_price_all_homes_data(self):
        data_file = open("data/Zip_MedianListingPrice_AllHomes.csv", "r")

        self.insert_median_listing_price_data(MEDIAN_LISTING_PRICE_ALL_HOMES_TABLE, data_file)

    def insert_median_listing_price_condo_data(self):
        data_file = open("data/Zip_MedianListingPrice_CondoCoop.csv", "r")

        self.insert_median_listing_price_data(MEDIAN_LISTING_PRICE_CONDO_TABLE, data_file)

    def insert_median_listing_price_duplex_triplex_data(self):
        data_file = open("data/Zip_MedianListingPrice_DuplexTriplex.csv", "r")

        self.insert_median_listing_price_data(MEDIAN_LISTING_PRICE_DUPLEX_TRIPLEX_TABLE, data_file)

    def insert_median_listing_price_sfr_data(self):
        data_file = open("data/Zip_MedianListingPrice_Sfr.csv", "r")

        self.insert_median_listing_price_data(MEDIAN_LISTING_PRICE_SFR_TABLE, data_file)

    def insert_data(self):
        # insert median listing price data
        self.insert_median_listing_price_all_homes_data()

        self.insert_median_listing_price_condo_data()

        self.insert_median_listing_price_duplex_triplex_data()

        self.insert_median_listing_price_sfr_data()
