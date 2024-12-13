import sqlite3

# create database connection
conn = sqlite3.connect('00_sqlite_tutorial/sample.db')
conn.close()


# in pratice, the most used way to connect and create it
with sqlite3.connect('00_sqlite_tutorial/sample.db') as conn:
    # any interaction with the database
    pass

# to catch an error if it occurs
try:
    with sqlite3.connect('00_sqlite_tutorial/sample.db') as conn:
        pass
except sqlite3.OperationalError as e:
    print(f'Failed to open the database: {e}')

