DROP TABLE IF EXISTS group_1_teams;

CREATE TABLE group_1_teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points VARCHAR(255)
);

DROP TABLE IF EXISTS group_2_teams;

CREATE TABLE group_2_teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points VARCHAR(255)
);