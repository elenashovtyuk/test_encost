import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

# Запрос на копирование со станков:
# “Фрезерный станок”, “Старый, ЧПУ”, “Сварка”,
# причины простоя и перенос их на новые станки.
cursor.execute(
    '''
    INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
    SELECT 7, reason_name, reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_reasons.endpoint_id = 6
    '''
)
cursor.execute(
    '''
    INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
    SELECT 8, reason_name, reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_reasons.endpoint_id = 5
    '''
)
cursor.execute(
    '''
    INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
    SELECT 9, reason_name, reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_reasons.endpoint_id = 1
    '''
)


data_2 = cursor.execute(
    '''
    SELECT * FROM endpoint_reasons;

    '''
)
for row in data_2:
    print(row)
