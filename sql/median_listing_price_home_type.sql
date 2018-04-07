# drop tables

DROP TABLE IF EXISTS median_listing_price_all_homes;
DROP TABLE IF EXISTS median_listing_price_condo;
DROP TABLE IF EXISTS median_listing_price_duplex_triplex;
DROP TABLE IF EXISTS median_listing_price_sfr;


# create median_listing_price_all_homes table

CREATE TABLE median_listing_price_all_homes (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create median_listing_price_condo table

CREATE TABLE median_listing_price_condo (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create median_listing_price_duplex_triplex table

CREATE TABLE median_listing_price_duplex_triplex (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create median_listing_price_sfr table

CREATE TABLE median_listing_price_sfr (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

