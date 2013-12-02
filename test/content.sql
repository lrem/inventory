INSERT INTO storage VALUES (0, 0, 'warehouse', NULL);
INSERT INTO storage VALUES (1, 0, 'left room', 'the one on the left');
INSERT INTO storage VALUES (2, 1, 'shelves', NULL);
INSERT INTO storage VALUES (3, 2, 'upper', NULL);
INSERT INTO storage VALUES (4, 2, 'lower', NULL);
INSERT INTO storage VALUES (5, 0, 'right room', 'the one on the right');
INSERT INTO storage VALUES (6, 5, 'thrash can', NULL);

-- And now the NULL-less style

INSERT INTO items (id, name, storage) VALUES (1, 'tools', 4);
INSERT INTO items (id, name, storage) VALUES (2, 'treasures', 3);
INSERT INTO items (id, name, storage) VALUES (3, 'thrash', 6);
