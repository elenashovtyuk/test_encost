import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    INSERT INTO endpoint_groups (endpoint_id, name)
    VALUES
        ((SELECT endpoints.id FROM endpoints
        WHERE endpoints.name = 'Сварочный аппарат №1'), 'Цех №2'),

        ((SELECT endpoints.id FROM endpoints
        WHERE endpoints.name = 'Пильный аппарат №2'), 'Цех №2'),

        ((SELECT endpoints.id FROM endpoints
        WHERE endpoints.name = 'Фрезер №3'), 'Цех №2')
    '''
)

data_3 = cursor.execute(
    '''
    SELECT * FROM endpoint_groups;

    '''
)

for row in data_3:
    print(row)
connection.commit()
cursor.close()
