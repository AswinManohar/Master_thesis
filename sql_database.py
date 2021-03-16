#!/usr/bin/env python


import sqlite3
from sqlite3 import Error
 
 
def create_connection(processed_files):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(processed_files)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("/u/aswin/database/Processed.db")
