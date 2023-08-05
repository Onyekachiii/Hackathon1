
-- -- DROP DATABASE IF EXISTS "Pokemon DB";

CREATE DATABASE "Pokemon DB"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default


CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE battles (
    battle_id SERIAL PRIMARY KEY,
    player1_id INTEGER REFERENCES players(player_id),
    player2_id INTEGER REFERENCES players(player_id),
    winner_id INTEGER REFERENCES players(player_id),
    battle_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE pokemons (
    pokemon_id SERIAL PRIMARY KEY,
    pokemon_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE player_pokemons (
    player_pokemon_id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(player_id),
    pokemon_id INTEGER REFERENCES pokemons(pokemon_id)

);

    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
