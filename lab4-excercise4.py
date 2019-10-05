import sqlite3
#connect to database file
dbconnect = sqlite3.connect("lab4.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''insert into table2 values (1, 'door', 'kitchen')''');
cursor.execute('''insert into table2 values (2, 'temperature', 'kitchen')''');
cursor.execute('''insert into table2 values (3, 'door', 'garage')''');
cursor.execute('''insert into table2 values (4, 'motion', 'garage')''');
cursor.execute('''insert into table2 values (5, 'temperature', 'garage')''');
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM table2');
print("Display all Kitchen sensors")
cursor.execute('SELECT * FROM table2 WHERE zone = "kitchen"');

for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );
print("Display all Door sensors")
    
cursor.execute('SELECT * FROM table2 WHERE type = "door"');
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );
#close the connection
dbconnect.close();
