# drop education data
DROP TABLE IF EXISTS education;

# create education table

CREATE TABLE education (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    less_than_high_school INT NOT NULL,
    bachelors INT NOT NULL,
    masters INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;