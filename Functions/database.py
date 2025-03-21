# This File Contains All Python Functions Used for Database

import sqlite3

"""
InitializeDatabase() Funtion

Parameters: Database File Path, Query File Path
Properties:
    - bool suppress_text : Change whether the function should print out debug text

Executes the SQL commands located in create_tables.sql 
file to create necessary tables for the database
"""
def InitializeDatabase(db_name, file_path, suppress_text=True):
    # Opens .sql File
    with open(file_path, 'r') as file:
        sql_queries = file.read()
    
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Executes the Queries
    cursor.executescript(sql_queries)
    
    # Commits Changes and Close Connection
    conn.commit()
    conn.close()
    if suppress_text == False:
        print(f"Database setup complete via {file_path}")

"""
PopulateDatabase() Funtion

Parameters: Database File Path, Query File Path
Properties:
    - bool suppress_text : Change whether the function should print out debug text

Executes the SQL commands located in populate_tables.sql 
file to populate the tables located in the database with
the information
"""
def PopulateDatabase(db_name, file_path, suppress_text=True):
    # Open the .sql file
    with open(file_path, 'r') as file:
        sql_queries = file.read()
    
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Executes the Queries
    cursor.executescript(sql_queries)
    
    # Commits Changes and Close Connection
    conn.commit()
    conn.close()
    if suppress_text == False:
        print(f"Database population complete from {file_path}")

"""
PrintCharacters() Funtion

Parameters: Database File Path

Grabs all the information in the characters table from the database
and prints it to the console
"""
def PrintCharacters(db_name):
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Executes Query to Grab Info
    cursor.execute("SELECT * FROM characters")

    # Grabs Results from Query
    rows = cursor.fetchall()

    # Prints Collumn Headers
    column_names = [description[0] for description in cursor.description]
    print("\t\t".join(column_names))

    # Prints Each Row in Table
    for row in rows:
        print("\t\t".join(str(value) for value in row))

    # Closes Connection
    conn.close()

"""
PrintSimpleCharacters() Funtion

Parameters: Database File Path

Grabs the name, side, type and rarity of all from the characters table
and prints it to the console
"""
def PrintSimpleCharacters(db_name):
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Executes Query to Grab Info
    cursor.execute("SELECT char_id, name, side, type, rarity FROM characters")

    # Grabs Results from Query
    rows = cursor.fetchall()

    # Prints Collumn Headers
    column_names = [description[0] for description in cursor.description]
    print("\t\t".join(column_names))

    # Prints Each Row in Table
    for row in rows:
        print("\t\t".join(str(value) for value in row))

    # Closes Connection
    conn.close()

"""
PrintLinks() Funtion

Parameters: Database File Path

Grabs all the information in the links_list table from the database
and prints it to the console
"""
def PrintLinks(db_name):
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Executes Query to Grab Info
    cursor.execute("SELECT * FROM links_list")

    # Grabs Results from Query
    rows = cursor.fetchall()

    # Prints Collumn Headers
    column_names = [description[0] for description in cursor.description]
    print("\t\t".join(column_names))

    # Prints Each Row in Table
    for row in rows:
        print("\t\t".join(str(value) for value in row))

    # Closes Connection
    conn.close()

"""
PrintCategories() Funtion

Parameters: Database File Path

Grabs all the information in the categories_list table from the database
and prints it to the console
"""
def PrintCategories(db_name):
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Executes Query to Grab Info
    cursor.execute("SELECT * FROM categories_list")

    # Grabs Results from Query
    rows = cursor.fetchall()

    # Prints Collumn Headers
    column_names = [description[0] for description in cursor.description]
    print("\t\t".join(column_names))

    # Prints Each Row in Table
    for row in rows:
        print("\t\t".join(str(value) for value in row))

    # Closes Connection
    conn.close()
