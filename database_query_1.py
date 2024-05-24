import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    SELECT endpoint_id, reason_name
    FROM
        endpoint_reasons INNER JOIN endpoints
        ON endpoint_reasons.endpoint_id = endpoints.id
    WHERE endpoints.active = 'true';
    '''
)

for result in cursor:
    print(result)
