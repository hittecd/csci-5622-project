from database_manager import DatabaseManager


ZIP_INDEX = 2
TOTAL_POPULATION_INDEX = 3

INSERT_TOTAL_POPULATION_TEMPLATE = "INSERT INTO total_population (zip_id, population) VALUES ({0}, {1});"
DELETE_TOTAL_POPULATION_TEMPLATE = "DELETE FROM total_population;"

zip_codes = [90895, 91001, 91006, 91007, 91011, 91010, 91016, 91020, 91017, 93510,
             91023, 91024, 91030, 91040, 91043, 91042, 91101, 91103, 91105, 93534,
             91104, 93532, 91107, 93536, 91106, 93535, 91108, 93543, 93544, 91123,
             93551, 93550, 93553, 93552, 91182, 93563, 91189, 91202, 91201, 93591,
             91204, 91203, 91206, 91205, 91208, 91207, 91210, 91214, 91302, 91301,
             91304, 91303, 91306, 91307, 91310, 92397, 91311, 91316, 91322, 91321,
             91325, 91324, 91326, 91331, 91330, 91335, 91340, 91343, 91342, 91345,
             91344, 91350, 91346, 91352, 91351, 91354, 91356, 91355, 91357, 91361,
             91364, 91367, 91365, 91381, 91384, 91387, 91390, 91402, 91401, 91403,
             91406, 91405, 91411, 91423, 91436, 91495, 91501, 91502, 91505, 91504,
             91506, 91602, 91601, 91604, 91606, 91605, 91608, 91607, 91614, 91706,
             91702, 91711, 91722, 91724, 91723, 91732, 91731, 91733, 91735, 91740,
             91741, 91745, 91744, 91747, 91746, 91748, 90002, 91750, 90001, 90004,
             91755, 91754, 90003, 90006, 90005, 90008, 91759, 90007, 90010, 90012,
             91765, 90011, 90014, 91767, 90013, 91766, 90016, 90015, 91768, 90018,
             90017, 91770, 90020, 91773, 90019, 91772, 91776, 90022, 90021, 91775,
             91780, 90024, 90023, 91778, 90026, 90025, 90028, 90027, 91790, 90029,
             91789, 90032, 91792, 91791, 90031, 90034, 90033, 91793, 90036, 90035,
             90038, 91801, 90037, 90040, 91803, 90039, 90042, 90041, 90044, 90043,
             90046, 90045, 90048, 90047, 90049, 90052, 90056, 90058, 90057, 90060,
             90059, 90062, 90061, 90064, 90063, 90066, 90065, 90068, 90067, 90069,
             90071, 90074, 90077, 91008, 90084, 90089, 90095, 90094, 90096, 90201,
             90189, 90211, 90210, 90212, 90221, 90220, 90222, 90230, 90232, 90241,
             90240, 90245, 90242, 90248, 90247, 90250, 90249, 90254, 90260, 90255,
             90262, 90263, 90266, 90265, 90270, 90274, 90272, 90277, 90275, 90280,
             90278, 90291, 90290, 90293, 90292, 90301, 90296, 90303, 90302, 90305,
             90304, 90402, 90401, 90404, 90403, 90406, 93243, 90405, 90501, 90503,
             90502, 90505, 90504, 90508, 90601, 90603, 90602, 90605, 90604, 90606,
             90631, 90639, 90638, 90650, 90640, 90660, 90670, 90702, 90701, 90704,
             90703, 90706, 90710, 90713, 90712, 90715, 90717, 90716, 90731, 90723,
             90733, 90732, 90745, 90744, 90747, 90746, 90755, 90803, 90802, 90805,
             90804, 90807, 90806, 90808, 90813, 90810, 90815, 90814, 90840]


class TotalPopulationDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete total population records
        cursor.execute(DELETE_TOTAL_POPULATION_TEMPLATE.format())

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

    def insert_data(self):
        # open file
        data_file = open("data/demographic/total_population.csv", "r")

        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # parse data lines
        data_lines = data_file.readlines()

        for data_line in data_lines[2:]:
            # split data line
            data_line = data_line.replace('\"', '').split(',')

            # get zip field from data line
            zip_data = data_line[ZIP_INDEX]
            zip_data = zip_data.split(' ')[1]

            # filter based on Los Angeles zips
            if int(zip_data) not in zip_codes:
                continue

            # get population data if zip is in LA list
            total_population_data = data_line[TOTAL_POPULATION_INDEX]

            # get parent record objects
            state = self.state_dao.insert_data("CA")
            county = self.county_dao.insert_data(state.state_id, "Los Angeles")
            metro = self.metro_dao.insert_data(state.state_id, "Los Angeles-Long Beach-Anaheim")
            city = self.city_dao.insert_data(county.county_id, metro.metro_id, state.state_id, "Los Angeles")
            zip_code = self.zip_dao.insert_data(city.city_id,
                                                county.county_id,
                                                metro.metro_id,
                                                state.state_id,
                                                zip_data)

            # insert total population records
            cursor.execute(INSERT_TOTAL_POPULATION_TEMPLATE.format(zip_code.zip_id, int(total_population_data)))

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()
