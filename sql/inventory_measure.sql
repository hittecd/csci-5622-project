# drop tables

DROP TABLE IF EXISTS inventory_measure;
DROP TABLE IF EXISTS inventory_measure_ssa;


# create inventory_measure table

CREATE TABLE inventory_measure (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    inventory INT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;


# create inventory_measure_ssa table

CREATE TABLE inventory_measure_ssa (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    date_time DATE NOT NULL,
    inventory INT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
