from state import StateDAO, State
from county import CountyDAO, County
from metro import MetroDAO, Metro
from city import CityDAO, City
from zip import ZipDAO, Zip

from food_stamps import FoodStampsDAO
from median_income import MedianIncomeDAO
from relationships import RelationshipsDAO
from total_population import TotalPopulationDAO
from transportation_method import TransportationMethodDAO
from education import EducationDAO
from language_spoken import LanguageSpokenDAO
from age_race_sex import AgeRaceSexDAO


if __name__ == "__main__":
    # initialize DAOs
    state_dao = StateDAO()
    county_dao = CountyDAO()
    metro_dao = MetroDAO()
    city_dao = CityDAO()
    zip_dao = ZipDAO()

    food_stamps_dao = FoodStampsDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    median_income_dao = MedianIncomeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    relationships_dao = RelationshipsDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    total_population_dao = TotalPopulationDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    transportation_method_dao = TransportationMethodDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    education_dao = EducationDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    languanges_spoken_dao = LanguageSpokenDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    age_race_sex_dao = AgeRaceSexDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)

    food_stamps_dao.delete_data()
    median_income_dao.delete_data()
    relationships_dao.delete_data()
    total_population_dao.delete_data()
    transportation_method_dao.delete_data()
    education_dao.delete_data()
    languanges_spoken_dao.delete_data()
    age_race_sex_dao.delete_data()

    # insert records
    food_stamps_dao.insert_data()
    median_income_dao.insert_data()
    relationships_dao.insert_data()
    total_population_dao.insert_data()
    transportation_method_dao.insert_data()
    education_dao.insert_data()
    languanges_spoken_dao.insert_data()
    age_race_sex_dao.insert_data()
