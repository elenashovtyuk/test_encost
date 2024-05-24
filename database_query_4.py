import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    INSERT INTO endpoints (name, active)

    VALUES
        ('Сварочный аппарат №1', 'true'),
        ('Пильный аппарат №2', 'true'),
        ('Фрезер №3', 'true');

    '''
)

data = cursor.execute(
    '''
    SELECT DISTINCT name, active FROM endpoints;

    '''
)

for row in data:
    print(row)
connection.commit()
cursor.close()
