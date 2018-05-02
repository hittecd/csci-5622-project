# drop age, race, and sex data
DROP TABLE IF EXISTS age_race_sex;

# create age_race_sex table

CREATE TABLE age_race_sex (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    male INT NOT NULL,
    female INT NOT NULL,
    percent_white DECIMAL(12, 2) NOT NULL,
    percent_black DECIMAL(12, 2) NOT NULL,
    percent_asian DECIMAL(12, 2) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;