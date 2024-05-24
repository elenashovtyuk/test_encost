import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    UPDATE endpoint_groups
    SET name = 'Цех №2'
    WHERE endpoint_id IN (
        SELECT id FROM endpoints WHERE name = 'Пильный станок'
        OR name = 'Старый ЧПУ'
    );
    '''
)

data_4 = cursor.execute(
    '''
    SELECT * FROM endpoint_groups;

    '''
)

for row in data_4:
    print(row)
connection.commit()
cursor.close()
