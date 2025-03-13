from Functions.database import InitializeDatabase, PopulateDatabase, PrintCharacters

db_file = 'Database/dokkan_battle.db'  # Name of your SQLite database file
create_file = 'Database/create_tables.sql'  # Path to your SQL file
populate_file = 'Database/populate_tables.sql'

print("Welcome to MyDokkanInfo")
InitializeDatabase(db_file, create_file)
PopulateDatabase(db_file, populate_file)
PrintCharacters(db_file)