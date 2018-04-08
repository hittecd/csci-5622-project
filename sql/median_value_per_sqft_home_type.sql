# drop tables

DROP TABLE IF EXISTS median_value_per_sqft_all_homes;


# create median_value_per_sqft_all_homes table

CREATE TABLE median_value_per_sqft_all_homes (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
