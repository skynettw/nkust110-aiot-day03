import sqlite3
db = sqlite3.connect("nkustnews.db")
sql = "select * from news;"
rows = db.execute(sql)
for row in rows:
    print(row[1])
        