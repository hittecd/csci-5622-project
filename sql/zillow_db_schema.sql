# drop constraints

ALTER TABLE county DROP FOREIGN KEY county_ibfk_1;

ALTER TABLE metro DROP FOREIGN KEY metro_ibfk_1;

ALTER TABLE city DROP FOREIGN KEY city_ibfk_1;
ALTER TABLE city DROP FOREIGN KEY city_ibfk_2;
ALTER TABLE city DROP FOREIGN KEY city_ibfk_3;

ALTER TABLE zip DROP FOREIGN KEY zip_ibfk_1;
ALTER TABLE zip DROP FOREIGN KEY zip_ibfk_2;
ALTER TABLE zip DROP FOREIGN KEY zip_ibfk_3;
ALTER TABLE zip DROP FOREIGN KEY zip_ibfk_4;


ALTER TABLE median_listing_price_one_room DROP FOREIGN KEY median_listing_price_one_room_ibfk_1;
ALTER TABLE median_listing_price_two_room DROP FOREIGN KEY median_listing_price_two_room_ibfk_1;
ALTER TABLE median_listing_price_three_room DROP FOREIGN KEY median_listing_price_three_room_ibfk_1;
ALTER TABLE median_listing_price_four_room DROP FOREIGN KEY median_listing_price_four_room_ibfk_1;
ALTER TABLE median_listing_price_five_plus_room DROP FOREIGN KEY median_listing_price_five_plus_room_ibfk_1;

ALTER TABLE median_listing_price_per_sqft_one_room DROP FOREIGN KEY median_listing_price_per_sqft_one_room_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_two_room DROP FOREIGN KEY median_listing_price_per_sqft_two_room_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_three_room DROP FOREIGN KEY median_listing_price_per_sqft_three_room_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_four_room DROP FOREIGN KEY median_listing_price_per_sqft_four_room_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_five_plus_room DROP FOREIGN KEY median_listing_price_per_sqft_five_plus_room_ibfk_1;

ALTER TABLE median_listing_price_all_homes DROP FOREIGN KEY median_listing_price_all_homes_ibfk_1;
ALTER TABLE median_listing_price_condo DROP FOREIGN KEY median_listing_price_condo_ibfk_1;
ALTER TABLE median_listing_price_duplex_triplex DROP FOREIGN KEY median_listing_price_duplex_triplex_ibfk_1;
ALTER TABLE median_listing_price_sfr DROP FOREIGN KEY median_listing_price_sfr_ibfk_1;

ALTER TABLE median_listing_price_per_sqft_all_homes DROP FOREIGN KEY median_listing_price_per_sqft_all_homes_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_condo DROP FOREIGN KEY median_listing_price_per_sqft_condo_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_duplex_triplex DROP FOREIGN KEY median_listing_price_per_sqft_duplex_triplex_ibfk_1;
ALTER TABLE median_listing_price_per_sqft_sfr DROP FOREIGN KEY median_listing_price_per_sqft_sfr_ibfk_1;

ALTER TABLE listing_price_cut_season_adj_all_homes DROP FOREIGN KEY listing_price_cut_season_adj_all_homes_ibfk_1;
ALTER TABLE listing_price_cut_season_adj_condo DROP FOREIGN KEY listing_price_cut_season_adj_condo_ibfk_1;
ALTER TABLE listing_price_cut_season_adj_sfr DROP FOREIGN KEY listing_price_cut_season_adj_sfr_ibfk_1;

ALTER TABLE median_price_cut_dollar_all_homes DROP FOREIGN KEY median_price_cut_dollar_all_homes_ibfk_1;
ALTER TABLE median_price_cut_dollar_condo DROP FOREIGN KEY median_price_cut_dollar_condo_ibfk_1;
ALTER TABLE median_price_cut_dollar_sfr DROP FOREIGN KEY median_price_cut_dollar_sfr_ibfk_1;

ALTER TABLE median_percent_price_reduction_all_homes DROP FOREIGN KEY median_percent_price_reduction_all_homes_ibfk_1;
ALTER TABLE median_percent_price_reduction_condo DROP FOREIGN KEY median_percent_price_reduction_condo_ibfk_1;
ALTER TABLE median_percent_price_reduction_sfr DROP FOREIGN KEY median_percent_price_reduction_sfr_ibfk_1;

ALTER TABLE median_value_per_sqft_home_type DROP FOREIGN KEY median_value_per_sqft_home_type_ibfk_1;

ALTER TABLE percent_listings_price_reduction_all_homes DROP FOREIGN KEY percent_listings_price_reduction_all_homes_ibfk_1;
ALTER TABLE percent_listings_price_reduction_condo DROP FOREIGN KEY percent_listings_price_reduction_condo_ibfk_1;
ALTER TABLE percent_listings_price_reduction_sfr DROP FOREIGN KEY percent_listings_price_reduction_sfr_ibfk_1;

# drop tables

DROP TABLE IF EXISTS state;
DROP TABLE IF EXISTS county;
DROP TABLE IF EXISTS metro;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS zip;


# create state table

CREATE TABLE state (
    id INT NOT NULL AUTO_INCREMENT,
    state_name VARCHAR(2) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX(state_name)
) ENGINE=INNODB;


# create county table

CREATE TABLE county (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    county_name VARCHAR(128) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX(state_id, county_name),
    FOREIGN KEY (state_id)
        REFERENCES state(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create metro table

CREATE TABLE metro (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    metro_name VARCHAR(128) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX(state_id, metro_name),
    FOREIGN KEY (state_id)
        REFERENCES state(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create city table

CREATE TABLE city (
    id INT NOT NULL AUTO_INCREMENT,
    county_id INT NOT NULL,
    metro_id INT NOT NULL,
    state_id INT NOT NULL,
    city_name VARCHAR(128) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX(state_id, city_name),
    FOREIGN KEY (county_id)
        REFERENCES county(id)
        ON DELETE CASCADE,
    FOREIGN KEY (metro_id)
        REFERENCES metro(id)
        ON DELETE CASCADE,
    FOREIGN KEY (state_id)
        REFERENCES state(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create zip table

CREATE TABLE zip (
    id INT NOT NULL AUTO_INCREMENT,
    city_id INT NOT NULL,
    county_id INT NOT NULL,
    metro_id INT NOT NULL,
    state_id INT NOT NULL,
    zip_code VARCHAR(5) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX(city_id, county_id, metro_id, state_id, zip_code),
    FOREIGN KEY (city_id)
        REFERENCES city(id)
        ON DELETE CASCADE,
    FOREIGN KEY (county_id)
        REFERENCES county(id)
        ON DELETE CASCADE,
    FOREIGN KEY (metro_id)
        REFERENCES metro(id)
        ON DELETE CASCADE,
    FOREIGN KEY (state_id)
        REFERENCES state(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create median listing price tables
source median_listing_price_num_rooms.sql
source median_listing_price_per_sqft_num_rooms.sql
source median_listing_price_home_type.sql
source median_listing_price_per_sqft_home_type.sql
source listing_price_cut_season_adj_home_type.sql
source median_price_cut_dollar_home_type.sql
source median_percent_price_reduction_home_type.sql
source median_value_per_sqft_home_type.sql
source percent_listings_price_reduction_home_type.sql

