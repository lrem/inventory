INSERT INTO storage VALUES (1234, NULL, 'warehouse', NULL);
INSERT INTO storage VALUES (1, 0, 'left room', 'the one on the left');
INSERT INTO storage VALUES (2, 1, 'shelves', NULL);
INSERT INTO storage VALUES (3, 2, 'upper', NULL);
INSERT INTO storage VALUES (4, 2, 'lower', NULL);
INSERT INTO storage VALUES (5, 0, 'right room', 'the one on the right');
INSERT INTO storage VALUES (6, 5, 'thrash can', NULL);

-- And now the NULL-less style

INSERT INTO storage (name, parent) VALUES ('tools', 4);
INSERT INTO storage (name, parent) VALUES ('treasures', 3);
INSERT INTO storage (name, parent) VALUES ('thrash', 6);
