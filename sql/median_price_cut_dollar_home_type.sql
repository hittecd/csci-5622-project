# drop tables

DROP TABLE IF EXISTS median_price_cut_dollar_all_homes;
DROP TABLE IF EXISTS median_price_cut_dollar_condo;
DROP TABLE IF EXISTS median_price_cut_dollar_sfr;


# create median_price_cut_dollar_all_homes table

CREATE TABLE median_price_cut_dollar_all_homes (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price_cut DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create median_price_cut_dollar_condo table

CREATE TABLE median_price_cut_dollar_condo (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price_cut DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create median_price_cut_dollar_sfr table

CREATE TABLE median_price_cut_dollar_sfr (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price_cut DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

