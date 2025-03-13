# This File Contains All Python Functions Used for Database
import sqlite3

def InitializeDatabase(db_name, file_path):
    # Open the .sql file
    with open(file_path, 'r') as file:
        sql_queries = file.read()
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Execute the queries from the file
    cursor.executescript(sql_queries)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database setup complete from {file_path}")

def PopulateDatabase(db_name, file_path):
    # Open the .sql file
    with open(file_path, 'r') as file:
        sql_queries = file.read()
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Execute the queries from the file
    cursor.executescript(sql_queries)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database population complete from {file_path}")

def PrintCharacters(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Execute a query to fetch all data from the characters table
    cursor.execute("SELECT * FROM characters")

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    # Print the column names (for reference)
    column_names = [description[0] for description in cursor.description]
    print("\t\t".join(column_names))

    # Print each row in the characters table
    for row in rows:
        print("\t\t".join(str(value) for value in row))

    # Close the connection
    conn.close()
