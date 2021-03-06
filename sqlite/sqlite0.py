import sqlite3
"""
Create table and insert data
"""
conn = sqlite3.connect("mydb.db")

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# c.execute("INSERT INTO projects VALUES ('111','projectName','2020-08-28','2020-10-28')") # violate unique primary key
# Save (commit) the changes
conn.commit()

conn.close()

print("Done.")