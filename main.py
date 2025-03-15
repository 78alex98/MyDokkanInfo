from Functions.database import *                                # Contains All Functions Related to Database
from GUI.gui import *                                           # Contains All Functions Related to GUI

db_file = 'Database/dokkan_battle.db'                           # SQLite DataBase File Path
create_file = 'Database/create_tables.sql'                      # SQL File Path for Creating Database Tables

# SQL File Paths to Populate Database
char_file = 'Database/populate_char.sql'
stats_file = 'Database/populate_stats.sql'
leaders_file = 'Database/Details Tables SQL/populate_leader.sql'
passive_file = 'Database/Details Tables SQL/populate_passive.sql'
detailsconnect_file = 'Database/Details Tables SQL/connect_details.sql'
supers_file = 'Database/populate_supers.sql'
linkslist_file = 'Database/populate_linkslist.sql'
categorieslist_file = 'Database/populate_categorieslist.sql'
ezaconn_file = 'Database/connect_char.sql'

# Initialize Program & Database
print("Welcome to MyDokkanInfo")
InitializeDatabase(db_file, create_file)

# Populate Database
PopulateDatabase(db_file, char_file)
PopulateDatabase(db_file, stats_file)
PopulateDatabase(db_file, supers_file)
PopulateDatabase(db_file, linkslist_file)
PopulateDatabase(db_file, categorieslist_file)
PopulateDatabase(db_file, leaders_file)
PopulateDatabase(db_file, passive_file)
PopulateDatabase(db_file, detailsconnect_file)
PopulateDatabase(db_file, ezaconn_file)

# Print Database Info
PrintSimpleCharacters(db_file)

# Creates the GUI
CreateApp()