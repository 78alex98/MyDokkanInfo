-- Drop existing tables if they exist
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS links_list;
DROP TABLE IF EXISTS links_character;
DROP TABLE IF EXISTS categories_list;
DROP TABLE IF EXISTS categories_character;

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
CREATE TABLE IF NOT EXISTS links_character (
    link_id INTEGER,
    char_id INTEGER,
    FOREIGN KEY (char_id) REFERENCES characters(char_id) ON DELETE CASCADE,
    FOREIGN KEY (link_id) REFERENCES links_list(link_id) ON DELETE CASCADE,
    PRIMARY KEY (char_id, link_id)
);

-- Stores all categories in game
CREATE TABLE IF NOT EXISTS categories_list (
    category_id INTEGER PRIMARY KEY,
    category_name
);

-- Create categories_character table
-- Junction table between categories_list and characters
CREATE TABLE IF NOT EXISTS categories_character (
    category_id INTEGER,
    char_id INTEGER,
    FOREIGN KEY (char_id) REFERENCES characters(char_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories_list(category_id) ON DELETE CASCADE,
    PRIMARY KEY (char_id, category_id)
);