from Functions.database import *                        # Contains All Functions Related to Database

db_file = 'Database/dokkan_battle.db'                   # SQLite DataBase File Path
create_file = 'Database/create_tables.sql'              # SQL File Path for Creating Database Tables
populate_file = 'Database/populate_tables.sql'          # SQL File Path for Populating Database
linkslist_file = 'Database/populate_linkslist.sql'      # SQL File Path for Populating Links List Table

# Main Code
print("Welcome to MyDokkanInfo")
InitializeDatabase(db_file, create_file)
PopulateDatabase(db_file, populate_file)
PopulateDatabase(db_file, linkslist_file)
PrintCharacters(db_file)