import sqlite3
import MySQLdb

mysql_conn = MySQLdb.connect(
    host = "127.0.0.1",
    port = 3307,
    user = 'root',
    passwd = '12345678',
    db = 'nkustnews'
)
cursor = mysql_conn.cursor()
cursor.execute("SET NAMES 'utf8'")
cursor.execute("SET CHARACTER SET utf8")
db = sqlite3.connect("nkustnews.db")
sql = "select * from news;"
rows = db.execute(sql)
for row in rows:
    try:
        my_sql = "insert into news (title, content, date, url) values('{}','{}','{}','{}');".format(
            row[1], row[2], row[3], row[4]
        )
        cursor.execute(my_sql)
        mysql_conn.commit()
    except:
        pass
db.close()
mysql_conn.close()        