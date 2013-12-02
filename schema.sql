CREATE TABLE storage (
    id INTEGER PRIMARY KEY,
    parent INTEGER NOT NULL REFERENCES storage,
    name TEXT NOT NULL,
    description TEXT
);
