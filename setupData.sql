INSERT INTO arenas (arena_id, name, city) VALUES
('ARENA_BYU', 'Marriott Center', 'Provo, UT'),
('ARENA_PURDUE', 'Mackey Arena', 'West Lafayette, IN'),
('ARENA_HOUSTON', 'Fertitta Center', 'Houston, TX'),
('ARENA_MICHIGAN', 'Crisler Center', 'Ann Arbor, MI'),
('ARENA_FLORIDA', 'Exactech Arena', 'Gainesville, FL');

INSERT INTO teams (team_id, name, arena_id) VALUES
('TEAM_BYU', 'BYU Cougars', 'ARENA_BYU'),
('TEAM_PURDUE', 'Purdue Boilermakers', 'ARENA_PURDUE'),
('TEAM_HOUSTON', 'Houston Cougars', 'ARENA_HOUSTON'),
('TEAM_MICHIGAN', 'Michigan Wolverines', 'ARENA_MICHIGAN'),
('TEAM_FLORIDA', 'Florida Gators', 'ARENA_FLORIDA');

INSERT INTO players (player_id, player_name, team_id) VALUES
('PLY_BYU_1', 'Jaxson Robinson', 'TEAM_BYU'),
('PLY_BYU_2', 'Dallin Hall', 'TEAM_BYU'),
('PLY_BYU_3', 'Trevin Knell', 'TEAM_BYU'),
('PLY_BYU_4', 'Fousseyni Traore', 'TEAM_BYU'),
('PLY_BYU_5', 'Aly Khalifa', 'TEAM_BYU'),
('PLY_PUR_1', 'Zach Edey', 'TEAM_PURDUE'),
('PLY_PUR_2', 'Braden Smith', 'TEAM_PURDUE'),
('PLY_PUR_3', 'Fletcher Loyer', 'TEAM_PURDUE'),
('PLY_PUR_4', 'Trey Kaufman-Renn', 'TEAM_PURDUE'),
('PLY_PUR_5', 'Caleb Furst', 'TEAM_PURDUE'),
('PLY_HOU_1', 'Jamal Shead', 'TEAM_HOUSTON'),
('PLY_HOU_2', 'LJ Cryer', 'TEAM_HOUSTON'),
('PLY_HOU_3', 'Emanuel Sharp', 'TEAM_HOUSTON'),
('PLY_HOU_4', 'J''Wan Roberts', 'TEAM_HOUSTON'),
('PLY_HOU_5', 'Joseph Tugler', 'TEAM_HOUSTON'),
('PLY_MICH_1', 'Doug McDaniel', 'TEAM_MICHIGAN'),
('PLY_MICH_2', 'Terrance Williams II', 'TEAM_MICHIGAN'),
('PLY_MICH_3', 'Nimari Burnett', 'TEAM_MICHIGAN'),
('PLY_MICH_4', 'Tarris Reed Jr.', 'TEAM_MICHIGAN'),
('PLY_MICH_5', 'Jaelin Llewellyn', 'TEAM_MICHIGAN'),
('PLY_FLA_1', 'Alex Condon', 'TEAM_FLORIDA'),
('PLY_FLA_2', 'Thomas Haugh', 'TEAM_FLORIDA'),
('PLY_FLA_3', 'Rueben Chinyelu', 'TEAM_FLORIDA'),
('PLY_FLA_4', 'Micah Handlogten', 'TEAM_FLORIDA'),
('PLY_FLA_5', 'Will Richard', 'TEAM_FLORIDA');

INSERT INTO wins (team_id, season, win_count) VALUES
('TEAM_BYU', '2025-2026', 17),
('TEAM_PURDUE', '2025-2026', 22),
('TEAM_HOUSTON', '2025-2026', 21),
('TEAM_MICHIGAN', '2025-2026', 20),
('TEAM_FLORIDA', '2025-2026', 19);