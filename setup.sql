CREATE TABLE arenas (
    arena_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    arena_id TEXT NOT NULL,
    FOREIGN KEY (arena_id) REFERENCES arenas(arena_id)
);

CREATE TABLE players (
    player_id TEXT PRIMARY KEY,
    player_name TEXT NOT NULL,
    team_id TEXT NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE wins (
    win_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id TEXT NOT NULL,
    season TEXT NOT NULL,
    win_count INTEGER DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);