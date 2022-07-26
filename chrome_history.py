
import sqlite3

con = sqlite3.connect('C:\Users\$user\AppData\Local\Google\Chrome\User Data\Default\History')

c = con.cursor()

c.execute("select url, title, visit_count, last_visit_time from urls")
results = c.fetchall()

for r in results:
    print(r)

c.close()