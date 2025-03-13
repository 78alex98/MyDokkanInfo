DROP TABLE IF EXISTS characters;

-- Create characters table
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT
);

-- Insert some sample characters
INSERT INTO characters (name, type) 
VALUES 
('Goku', 'STR'),
('Vegeta', 'AGL'),
('Piccolo', 'INT');