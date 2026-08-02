CREATE TABLE IF NOT EXISTS playlists (
    id SERIAL PRIMARY KEY,
    sp_playlist_id VARCHAR(255) UNIQUE,
    playlist_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS songs (
    id SERIAL PRIMARY KEY,
    playlist_id INTEGER NOT NULL,
    song_name VARCHAR(255) NOT NULL,
    artist_name VARCHAR(255) NOT NULL,

    CONSTRAINT fk_playlist
        FOREIGN KEY (playlist_id)
        REFERENCES playlists(id)
        ON DELETE CASCADE
);