CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE exerciseplaces (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    description TEXT,
    monday TEXT,
    tuesday TEXT,
    wednesday TEXT,
    thursday TEXT,
    friday TEXT,
    saturday TEXT,
    sunday TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    exerciseplaces_id INTEGER REFERENCES exerciseplaces
    ON DELETE CASCADE,
    user_id INTEGER REFERENCES users,
    stars INTEGER,
    review TEXT,
    time TIMESTAMP
);

CREATE TABLE groupnames (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    exerciseplaces_id INTEGER REFERENCES exerciseplaces
    ON DELETE CASCADE,
    groupnames_id INTEGER REFERENCES groupnames,
    UNIQUE(exerciseplaces_id,groupnames_id)
);
