DROP TABLE IF EXISTS autoclaves;

CREATE TABLE autoclaves (
    id INTEGER PRIMARY KEY,
    mname VARCHAR(15),
    stat VARCHAR(10),
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    setting VARCHAR(15),
    endtime DATETIME
);