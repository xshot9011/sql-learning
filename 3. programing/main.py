import sqlite3

connection = sqlite3.connect('chinook.db')

print('success')

cur = connection.execute('SELECT * FROM Customers;')

for row in cur:
    print(row)
    # acess to column is row[index]

connection.close()
