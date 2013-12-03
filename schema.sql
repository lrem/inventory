CREATE TABLE storage (
    id INTEGER PRIMARY KEY,
    parent INTEGER REFERENCES storage,
    name TEXT NOT NULL,
    description TEXT
);
