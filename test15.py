import sqlite3
db = sqlite3.connect("nkustnews.db")
data = list()
sql = "select title from news;"
rows = db.execute(sql)
for row in rows:
    data.append(row[0])
data = ";".join(data)
print(len(data))
        