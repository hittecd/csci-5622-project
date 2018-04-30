# drop total population data
DROP TABLE IF EXISTS total_population;

# create total_population table

CREATE TABLE total_population (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    population INTEGER NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
