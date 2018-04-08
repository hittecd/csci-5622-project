# drop tables

DROP TABLE IF EXISTS listing_price_cut_season_adj_all_homes;
DROP TABLE IF EXISTS listing_price_cut_season_adj_condo;
DROP TABLE IF EXISTS listing_price_cut_season_adj_sfr;


# create listing_price_cut_season_adj_all_homes table

CREATE TABLE listing_price_cut_season_adj_all_homes (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price_cut DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create listing_price_cut_season_adj_condo table

CREATE TABLE listing_price_cut_season_adj_condo (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price_cut DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create listing_price_cut_season_adj_sfr table

CREATE TABLE listing_price_cut_season_adj_sfr (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price_cut DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

