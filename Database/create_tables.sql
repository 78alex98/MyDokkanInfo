-- Drop existing tables if they exist
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS links_list;
DROP TABLE IF EXISTS links_character;

-- Create characters table
CREATE TABLE IF NOT EXISTS characters (
    char_id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT
);

-- Create links_list table
-- Stores all links in game
CREATE TABLE IF NOT EXISTS links_list (
    link_id INTEGER PRIMARY KEY,
    link_name
);

-- Create links_character table
-- Junction table between links_list and characters
CREATE TABLE IF NOT EXISTS links_list (
    link_id INTEGER,
    char id INTEGER,
    FOREIGN KEY (char_id) REFERENCES characters(char_id) ON DELETE CASCADE,
    FOREIGN KEY (link_id) REFERENCES links_list(link_id) ON DELETE CASCADE,
    PRIMARY KEY (char_id, link_id)
);