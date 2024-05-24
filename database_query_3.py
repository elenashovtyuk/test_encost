import sqlite3

connection = sqlite3.connect('client.sqlite')
cursor = connection.cursor()

cursor.execute(
    '''
    SELECT
        endpoint_reasons.endpoint_id,
        endpoint_reasons.reason_hierarchy,
        COUNT(endpoint_reasons.reason_name) AS count_power_outages
    FROM
        endpoint_reasons INNER JOIN endpoints
        ON endpoint_reasons.endpoint_id = endpoints.id
    GROUP BY
        endpoint_reasons.endpoint_id,
        endpoint_reasons.reason_hierarchy,
        endpoint_reasons.reason_name
    HAVING
        endpoints.active = 'true'
        AND endpoint_reasons.reason_name = 'Перебои напряжения';

    '''
)

for result in cursor:
    print(result)
