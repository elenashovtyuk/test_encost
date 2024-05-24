import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    SELECT endpoint_id, COUNT(reason_name) AS count_reasons
    FROM
        endpoint_reasons INNER JOIN endpoints
        ON endpoint_reasons.endpoint_id = endpoints.id
    GROUP BY endpoint_reasons.endpoint_id
    HAVING endpoints.active = 'false';

    '''
)

for result in cursor:
    print(result)
