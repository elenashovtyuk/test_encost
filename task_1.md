## Задача 1

### Алгоритм решения проблемы отправки ежедневного почтового отчета:

1. Проверка логов сервера: Первым делом проверим логи задачи на сервере, которая отвечает за формирование и отправку ежедневного отчета. Это поможет установить, была ли задача успешно выполнена и был ли отчет сгенерирован.


2. Проверка скрипта Python: Если ошибок в логах выполнения задачи нет и отчет был сгенерирован, следующим шагом будет проверка скрипта Python, который отправляет отчет. Нужно убедиться, что код выполняется без ошибок, и что есть соответствующие обработчики ошибок для отлова исключений, связанных с отправкой почты.

3. Проверка почтового сервера: Если скрипт работает корректно и посылает сообщения, следует проверить настройки и логи почтового сервера. Возможно, выяснится, что сообщения отклоняются или попадают в очередь из-за проблем на почтовом сервере.

4. Контакт с клиентом: Необходимо убедиться, что у клиента правильно настроены фильтры почты и что ежедневный отчет не попал в папку со спамом или не был удален автоматическими правилами почтового клиента.

5. Внутренние проверки безопасности: Проверим нет ли каких-либо внутренних настроек безопасности, которые могли бы блокировать или задерживать отправку писем.

6. Тестовая отправка: Попробуем повторить отправку отчета вручную, чтобы увидеть, проходит ли почта.

#### В ответ клиенту можно написать:

"Здравствуйте, {% Имя клиента %},

Мы получили ваше сообщение о том, что ежедневный почтовый отчет не был доставлен. Мы приносим свои извинения за этот недочет и уже приступили к расследованию причин этой проблемы.

Мы сделаем все необходимое для того, чтобы определить и устранить проблему как можно скорее. Также мы отправим вам отчет вручную и удостоверимся, что вы получили необходимую информацию.
Благодарим вас за ваше терпение и понимание.

С уважением,
Елена (технический специалист поддержки)"

Если эта ситуация повторяется:

- Необходимо провести тщательный анализ системы, чтобы выявить корневую причину проблемы. Для этого заведём тикет в багтрекере или в системе по управлению задачами.

- Необходимо рассмотреть вариант улучшения обработки ошибок и стабильности скрипта или процесса, который генерирует и отправляет отчеты.

- Предусмотрим резервный план на случай проблем с отправкой почты (например, настроим второй почтовый сервер или подтверждение приема отчета клиентом).

- Сообщим клиенту о принимаемых долгосрочных мерах по улучшению надежности доставки отчетов и о предпринимаемых шагах для предотвращения дальнейших проблем.
