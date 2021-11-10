DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    group_id INT,
    points INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    team_1_id INT REFERENCES teams ON DELETE CASCADE,
    team_2_id INT REFERENCES teams ON DELETE CASCADE,
    team_1_runs INTEGER,
    team_2_runs INTEGER,
    game_date DATE
);
