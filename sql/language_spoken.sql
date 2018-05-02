# drop language spoken data
DROP TABLE IF EXISTS language_spoken;

# create language_spoken table

CREATE TABLE language_spoken (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    english_only INT NOT NULL,
    non_english INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;