# drop relationships data
DROP TABLE IF EXISTS relationships;

# create relationships table

CREATE TABLE relationships (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    family_households INT NOT NULL,
    nonfamily_households INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
