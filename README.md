# Тестовое задание на позицию IT-специалист технической поддержки

1. Клиент не получил ежедневный почтовый отчет (excel-файл, который формируется на
нашем сервере с помощью python, содержит в себе данные о простоях и работе).
    1) Какой по вашему мнению алгоритм решения проблемы?
    2) Что Вы ответите клиенту?
    3) Что делать если эта ситуация повторяется несколько раз?

    [Ссылка на файл](task_1.txt)

2. Требуется выполнить следующие задания:

    1) Написать запрос, который выводит причины простоя только активных станков.

    [Ссылка на файл](.database_query_1.py)

    2) Написать запрос, который выводит количество причин простоев для каждой
    неактивной точки.

    [Ссылка на файл ](.database_query_2.py)

    3) Написать запрос, который выведет для каждого активного оборудования, количество
    причины простоя “ Перебои напряжения” (нужно учесть что это надо сделать для каждой
    группы(reason_hierarchy))

    [Ссылка на файл](.database_query_3.py)

3. Клиент просит сделать интеграцию с 1С.Предприятие(в 95% случаев клиентские
запросы сначала попадают к Вам).
    1) Что Вы ему ответите?
    2) Ваш план действий после того как Вы ему ответили?

    [Ссылка на файл](task_2.txt)


4. Произошло серьезное падение сервера, которое продлилось несколько часов, у
множества клиентов не было данных за этот период:
    1) Что Вы ответите клиенту?

    [Ссылка на файл](task_3.txt)

5. Клиент не может попасть в личный кабинет (клиенту предоставляется логин/пароль),
ваши действия?

[Ссылка на файл](task_4.txt)

6. Есть огромный текстовый файл (более 100 ГБ - он точно не поместится в оперативной
памяти), состоящий из строк, как его оптимально обрабатывать? - Напишите код на
python.

7. Что бы вы ответили клиенту? С чего бы начали проверку?

[Ссылка на файл](task_5.txt)

8. Напишите Python скрипт который будет писать в базу данных client следующую
информацию:

    1)Добавить 3 станка: “Сварочный аппарат №1”, “Пильный аппарат №2”, “Фрезер №3”,
    сделать их активными.

    [Ссылка на файл](.database_query_4.py)

    2)Скопировать со станков: “Фрезерный станок”, “Старый, ЧПУ”, “Сварка”, причины
    простоя и перенести их на новые станки.

    [Ссылка на файл](.database_query_5.py)

    3)Определить группу “Цех №2” для новых станков.

    [Ссылка на файл](.database_query_6.py)

    4)Добавить станки “Пильный станок” и “Старый ЧПУ” к новой группе.

    [Ссылка на файл](.database_query_7.py)
