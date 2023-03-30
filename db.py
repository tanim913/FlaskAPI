import sqlite3
conn = sqlite3.connect("musics.sqlite")

cursor = conn.cursor()

sql_query = """CREATE TABLE music (
    id integer PRIMARY KEY,
    artist text NOT NULL,
    language text NOT NULL,
    title text NOT NULL,
    test_num integer NOT NULL
)"""
cursor.execute(sql_query)
