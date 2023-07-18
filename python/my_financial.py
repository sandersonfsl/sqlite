import sqlite3

db = sqlite3.connect("my_financial.db")

cursor = db.cursor()

cursor.execute("CREATE TABLE expenses (day int,month int,year int,value real,expense text,category text,source text,payment text)")

cursor.execute("INSERT INTO expenses VALUES(1,1,2023,500,'gas','car','debit card','none')")

db.commit()

cursor.execute("SELECT * FROM expenses")

print(cursor.fetchall())
