import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
    SELECT 7,
    reason_name,
    reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_reasons.endpoint_id IN(
        SELECT endpoint_id
        FROM endpoints INNER JOIN endpoint_reasons ON
        endpoints.id = endpoint_reasons.endpoint_id
        WHERE endpoints.name = 'Сварка'
    )
    '''
)
cursor.execute(
    '''
    INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
    SELECT 8, reason_name, reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_reasons.endpoint_id IN(
        SELECT endpoint_id
        FROM endpoints INNER JOIN endpoint_reasons ON
        endpoints.id = endpoint_reasons.endpoint_id
        WHERE endpoints.name = 'Старый ЧПУ'
    )
    '''
)
cursor.execute(
    '''
    INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
    SELECT 9, reason_name, reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_reasons.endpoint_id IN(
        SELECT endpoint_id
        FROM endpoints INNER JOIN endpoint_reasons ON
        endpoints.id = endpoint_reasons.endpoint_id
        WHERE endpoints.name = 'Фрезерный станок'
    )
    '''
)

data_2 = cursor.execute(
    '''
    SELECT * FROM endpoint_reasons;

    '''
)

for row in data_2:
    print(row)
