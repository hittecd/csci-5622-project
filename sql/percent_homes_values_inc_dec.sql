# drop tables

DROP TABLE IF EXISTS percent_homes_values_increasing;
DROP TABLE IF EXISTS percent_homes_values_decreasing;


# create percent_homes_values_increasing table

CREATE TABLE percent_homes_values_increasing (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create percent_homes_values_decreasing table

CREATE TABLE percent_homes_values_decreasing (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    price DECIMAL(12, 2) NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

