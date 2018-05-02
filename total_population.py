from database_manager import DatabaseManager


ZIP_INDEX = 2
TOTAL_POPULATION_INDEX = 3

INSERT_TOTAL_POPULATION_TEMPLATE = "INSERT INTO total_population (zip_id, population) VALUES ({0}, {1});"
DELETE_TOTAL_POPULATION_TEMPLATE = "DELETE FROM total_population;"

zip_codes = [90401, 93534, 91306, 93560, 90008, 90014, 90094, 90822, 91326, 90212, 90001, 92624, 90006, 92617, 90301, 92655, 91401, 90803, 90095, 91203, 90021, 91801, 90089, 93225, 93550, 90057, 90723, 91723, 90278, 90079, 92844, 90029, 90502, 90036, 90265, 90270, 90716, 90743, 90745, 92371, 92055, 91046, 92661, 91202, 91210, 92782, 92865, 91330, 93252, 91371, 91390, 91411, 91601, 93532, 91607, 91702, 91755, 90302, 90403, 90073, 90254, 90715, 90742, 92649, 91340, 91602, 90503, 90220, 92692, 92646, 90404, 90071, 91803, 91384, 90039, 90011, 90807, 92691, 90248, 90703, 91303, 90020, 92614, 90201, 91780, 93563, 90732, 90405, 92620, 92397, 91342, 90077, 92869, 90250, 90061, 91361, 93552, 90015, 90002, 92679, 90022, 90041, 90211, 90059, 90066, 90210, 92887, 91343, 90062, 91606, 91403, 90605, 92694, 90063, 90012, 92835, 91768, 91745, 91307, 92530, 90293, 91402, 92807, 90242, 91364, 90631, 90040, 90007, 91331, 91103, 90005, 92676, 91362, 91040, 92805, 91770, 91790, 91776, 90031, 93591, 90305, 92604, 91324, 92648, 90304, 91010, 93040, 92867, 91724, 90043, 91316, 92780, 90280, 91710, 91352, 92701, 91011, 90069, 91325, 91208, 90262, 90621, 92612, 91344, 91030, 90222, 90713, 90019, 90680, 93243, 92801, 90290, 90056, 90706, 90032, 92883, 91381, 90291, 91731, 90260, 90027, 91302, 90247, 92627, 90232, 90013, 90701, 91789, 90042, 93544, 90221, 92301, 90035, 90024, 90026, 90034, 90016, 90018, 90004, 91502, 93553, 90747, 90067, 90010, 92821, 90025, 90047, 90813, 90303, 90037, 92562, 92625, 92886, 91605, 90049, 92861, 92831, 91006, 90744, 90241, 91351, 91007, 92870, 90606, 90028, 91506, 90640, 90263, 90266, 90272, 90275, 90623, 90650, 90630, 92672, 92630, 90806, 92372, 90731, 90805, 90740, 90746, 90755, 90802, 90670, 90710, 90712, 92660, 92663, 92675, 92677, 91016, 91020, 92602, 92603, 91042, 91101, 92678, 92618, 91106, 92626, 92637, 92647, 92683, 92651, 92653, 92656, 92657, 90814, 90831, 91001, 91008, 91345, 91350, 92880, 92881, 92882, 93063, 90003, 91205, 92704, 92705, 92706, 92707, 91206, 91301, 91321, 92802, 92804, 92806, 92808, 92823, 92832, 92833, 92840, 92841, 92843, 91335, 92866, 92868, 91304, 91207, 91107, 91108, 91201, 91311, 91214, 92703, 91204, 91604, 91608, 91709, 93510, 93523, 93535, 93536, 93543, 93551, 91405, 91367, 91406, 91377, 91436, 91387, 90506, 91504, 91423, 91505, 90274, 91356, 91748, 90292, 91750, 91773, 90402, 91775, 91754, 90065, 91759, 90501, 90230, 90048, 90504, 91765, 91767, 91740, 90046, 90038, 91711, 91722, 91741, 90044, 91732, 91733, 92708, 90808, 92629, 91355, 90810, 91354, 90245, 90660, 90720, 90602, 90603, 91791, 90255, 90604, 91792, 90240, 90638, 91744, 90023, 91763, 90068, 91746, 90045, 90601, 90620, 91784, 90815, 90717, 92673, 90804, 90505, 91706, 92688, 90064, 90704, 91105, 92610, 90058, 90249, 90033, 92606, 90017, 90277, 91104, 91501, 91766, 91024, 92845, 90090, 92662]

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
