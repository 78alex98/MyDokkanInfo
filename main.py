from Functions.database import InitializeDatabase, PrintCharacters

db_file = 'Database/dokkan_battle.db'  # Name of your SQLite database file
sql_file = 'Database/create_tables.sql'  # Path to your SQL file

print("Welcome to MyDokkanInfo")
InitializeDatabase(sql_file, db_file)
PrintCharacters(db_file)