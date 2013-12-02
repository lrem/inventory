CREATE TABLE storage (
    id INTEGER PRIMARY KEY,
    parent INTEGER NOT NULL REFERENCES storage,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    storage INTEGER NOT NULL REFERENCES storage,
    description TEXT
);
