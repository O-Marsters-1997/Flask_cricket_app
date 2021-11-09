DROP TABLE IF EXISTS group_1_games;
DROP TABLE IF EXISTS group_2_games;
DROP TABLE IF EXISTS group_1_teams;
DROP TABLE IF EXISTS group_2_teams;



CREATE TABLE group_1_teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);


CREATE TABLE group_2_teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);


CREATE TABLE group_1_games (
    id SERIAL PRIMARY KEY,
    team_1_id INT REFERENCES group_1_teams,
    team_2_id INT REFERENCES group_1_teams,
    team_1_runs INTEGER,
    team_2_runs INTEGER,
    game_date TIMESTAMP
);

CREATE TABLE group_2_games (
    id SERIAL PRIMARY KEY,
    team_1_id INT REFERENCES group_2_teams,
    team_2_id INT REFERENCES group_2_teams,
    team_1_runs INTEGER,
    team_2_runs INTEGER,
    game_date TIMESTAMP
);