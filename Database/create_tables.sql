-- Drop existing tables if they exist
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS links_list;
DROP TABLE IF EXISTS links_character;
DROP TABLE IF EXISTS categories_list;
DROP TABLE IF EXISTS categories_character;
DROP TABLE IF EXISTS details_leader;
DROP TABLE IF EXISTS details_passive;
DROP TABLE IF EXISTS details_combined;

-- Create characters table
CREATE TABLE IF NOT EXISTS characters (
    char_id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT
);

-- Create details_leader table
-- Stores Leader Skill Details
CREATE TABLE IF NOT EXISTS details_leader (
    leader_id INTEGER PRIMARY KEY,
    cat1 INTEGER,
    cat2 INTEGER,
    cat3 INTEGER,
    Ki_Buff TEXT,
    HP_Buff TEXT,
    ATK_Buff TEXT,
    DEF_Buff TEXT,
    Sub_cat1 INTEGER,
    Sub_cat2 INTEGER,
    Sub_cat3 INTEGER,
    Sub_Ki_Buff TEXT,
    Sub_HP_Buff TEXT,
    Sub_ATK_Buff TEXT,
    Sub_DEF_Buff TEXT
);

-- Create details_passive table
-- Stores Passive Skill Details
CREATE TABLE IF NOT EXISTS details_passive (
    passive_id INTEGER,
    passive_desc TEXT,
    has_active INTEGER,
    active_cond TEXT,
    has_standby INTEGER,
    standby_cond TEXT,
    result_skill TEXT
);

CREATE TABLE IF NOT EXISTS details_combined (
    details_id INTEGER,
    char_id INTEGER,
    leader1_id INTEGER,
    leader2_id INTEGER,
    passive_id INTEGER,
    FOREIGN KEY (char_id) REFERENCES characters(char_id) ON DELETE CASCADE,
    FOREIGN KEY (leader1_id) REFERENCES details_leader(leader_id) ON DELETE CASCADE,
    FOREIGN KEY (leader2_id) REFERENCES details_leader(leader_id) ON DELETE CASCADE,
    FOREIGN KEY (passive_id) REFERENCES details_passive(passive_id) ON DELETE CASCADE,
    PRIMARY KEY (char_id, leader1_id, passive_id)
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