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
    zip_code INT NOT NULL,
    PRIMARY KEY(id),
    UNIQUE INDEX(zip_code),
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
