# Telegram-Бот для пиццерии.
Имеет пассивную функцию удаления сообщений, содержащих маты.
## Команды бота: 
+ /start or /help  - Приветственное сообщение бота.
+ /Меню - Команда для отправки меню из базы данных.
+ /Режим_работы - Команда для получения времени работы пиццерии.
+ /Расположение - Команда для получения адреса пиццерии.
+ Отправить свой номер телефона - Команда для функции телеграмма отправки контакта.
+ Отправить свое местоположение - Команда для функции телеграмма отправки геолокации.
+ /Админ_панель - Команда для доступа к управлению базой данных с меню.
### Команды админ-панели:
+ /Добавить_пункт_меню - Запускает машину состояния пошагового добавления пункта меню.
+ /Отмена - Отменяет работу с админ-панелью или прерывает работы машины состояний.
+ /Удалить - Команда для удаления пункта меню через Inline-клавиатуру.

Команды админ-панели доступны только внесенным администраторам.
## Запуск.
Для запуска с `ubuntu` достаточно в файле `runbot.sh` заменить положение репозитория на действительное и заменить значение переменной `TOKEN` на токен вашего бота. После чего открыть в терминале эту директорию и прописать команду `source runbot.sh`.

Для запуска с `Windows` потребуется через `Python` модуль `venv` создать виртуальное окружение в папке скелет `python -m venv venv`, после чего создать файл с расширением `.bat` со следующим текстом:
```Bat
@echo off

call %~dp0skelet\venv\scripts\activate

cd %~dp0skelet

set TOKEN=

python bot_telegram.py

pause
```
Где переменной `TOKEN` так же нужно присвоить значение токена, полученного при создании бота. Файл необходимо поместить рядом с `runbot.sh`. Запустить можно двойным кликом мыши.


В файле `skelet\handlers\admin.py` в переменной
```Python
admin_ID = []
```
нужно через запятую указать ID администраторов и оставить в качестве списка.