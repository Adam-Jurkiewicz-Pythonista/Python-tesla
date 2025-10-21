import sqlite3
con = sqlite3.connect("users.db")

cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print(tables)


