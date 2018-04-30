# drop food stamps data
DROP TABLE IF EXISTS food_stamps;

# create food_stamps table

CREATE TABLE food_stamps (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    recipient_count INTEGER NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
