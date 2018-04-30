# drop transportation method data
DROP TABLE IF EXISTS transportation_method;

# create transportation_method table

CREATE TABLE transportation_method (
    id INT NOT NULL AUTO_INCREMENT,
    zip_id INT NOT NULL,
    personal_vehicle INT NOT NULL,
    carpool INT NOT NULL,
    public_transportation INT NOT NULL,
    taxi INT NOT NULL,
    motorcycle INT NOT NULL,
    walking INT NOT NULL,
    bicycle INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (zip_id)
        REFERENCES zip(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
