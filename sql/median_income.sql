# drop median income data
DROP TABLE IF EXISTS median_income;

# create median_income table

CREATE TABLE median_income (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    median_income INTEGER NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
