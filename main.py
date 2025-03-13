from Functions.database import *                                # Contains All Functions Related to Database

db_file = 'Database/dokkan_battle.db'                           # SQLite DataBase File Path
create_file = 'Database/create_tables.sql'                      # SQL File Path for Creating Database Tables

# SQL File Paths to Populate Database
populate_file = 'Database/populate_tables.sql'
linkslist_file = 'Database/populate_linkslist.sql'
categorieslist_file = 'Database/populate_categorieslist.sql'
leaders_file = 'Database/Details Tables SQL/populate_leader.sql'
passive_file = 'Database/Details Tables SQL/populate_passive.sql'
detailsconnect_file = 'Database/Details Tables SQL/connect_details.sql'


# Main Code
print("Welcome to MyDokkanInfo")
InitializeDatabase(db_file, create_file)

PopulateDatabase(db_file, populate_file)
PopulateDatabase(db_file, linkslist_file)
PopulateDatabase(db_file, categorieslist_file)
PopulateDatabase(db_file, leaders_file)
PopulateDatabase(db_file, passive_file)
PopulateDatabase(db_file, detailsconnect_file)

PrintCharacters(db_file)