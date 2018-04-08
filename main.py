from state import StateDAO, State
from county import CountyDAO, County
from metro import MetroDAO, Metro
from city import CityDAO, City
from zip import ZipDAO, Zip

from median_listing_price_num_rooms import MedianListingPriceNumBedroomsDAO
from median_listing_price_per_sqft_num_rooms import MedianListingPricePerSqftNumBedroomsDAO
from median_listing_price_home_type import MedianListingPriceHomeTypeDAO
from median_listing_price_per_sqft_home_type import MedianListingPricePerSqftHomeTypeDAO
from listing_price_cut_season_adj_home_type import ListingPriceCutSeasonAdjHomeTypeDAO
from median_price_cut_dollar_home_type import MedianPriceCutDollarHomeTypeDAO
from median_percent_price_reduction_home_type import MedianPercentPriceReductionHomeTypeDAO
from median_value_per_sqft_home_type import MedianValuePerSqftHomeTypeDAO;
from percent_listings_price_reduction_home_type import PercentListingsPriceReductionHomeTypeDAO;


if __name__ == "__main__":
    # initialize DAOs
    state_dao = StateDAO()
    county_dao = CountyDAO()
    metro_dao = MetroDAO()
    city_dao = CityDAO()
    zip_dao = ZipDAO()

    #median_listing_price_num_bedrooms_dao = MedianListingPriceNumBedroomsDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    #median_listing_price_per_sqft_num_bedrooms_dao = MedianListingPricePerSqftNumBedroomsDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    #median_listing_price_home_type_dao = MedianListingPriceHomeTypeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    #median_listing_price_per_sqft_home_type_dao = MedianListingPricePerSqftHomeTypeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    #listing_price_cut_season_adj_home_type_dao = ListingPriceCutSeasonAdjHomeTypeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    #median_price_cut_dollar_home_type_dao = MedianPriceCutDollarHomeTypeDAO(state_dao, county_dao, metro_dao,city_dao, zip_dao)
    #median_percent_price_reduction_home_type_dao = MedianPercentPriceReductionHomeTypeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    #median_value_per_sqft_home_type_dao = MedianValuePerSqftHomeTypeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)
    percent_listings_price_reduction_home_type_dao = PercentListingsPriceReductionHomeTypeDAO(state_dao, county_dao, metro_dao, city_dao, zip_dao)

    # delete all records
    #state_dao.delete_data()
    #county_dao.delete_data()
    #metro_dao.delete_data()
    #city_dao.delete_data()
    #zip_dao.delete_data()

    #median_listing_price_num_bedrooms_dao.delete_data()
    #median_listing_price_per_sqft_num_bedrooms_dao.delete_data()
    #median_listing_price_home_type_dao.delete_data()
    #median_listing_price_per_sqft_home_type_dao.delete_data()
    #listing_price_cut_season_adj_home_type_dao.delete_data()
    #median_price_cut_dollar_home_type_dao.delete_data()
    #median_percent_price_reduction_home_type_dao.delete_data()
    #median_value_per_sqft_home_type_dao.delete_data()
    percent_listings_price_reduction_home_type_dao.delete_data()

    # insert records
    #median_listing_price_num_bedrooms_dao.insert_data()
    #median_listing_price_per_sqft_num_bedrooms_dao.insert_data()
    #median_listing_price_home_type_dao.insert_data()
    #median_listing_price_per_sqft_home_type_dao.insert_data()
    #listing_price_cut_season_adj_home_type_dao.insert_data()
    #median_price_cut_dollar_home_type_dao.insert_data()
    #median_percent_price_reduction_home_type_dao.insert_data()
    #median_value_per_sqft_home_type_dao.insert_data()
    percent_listings_price_reduction_home_type_dao.insert_data()
