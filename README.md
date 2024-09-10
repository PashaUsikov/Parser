# Парсинг сайтов
Это WEB-приложение, которое по заданным пользователем категориям, мониторит (парсит) сайт Дром. Результат парсинга - объявления можно посмотреть на странице сайте.

## Установка

Скачайте проект с githab:
```
git clone https://
```

Создайте виртуальное окружение и установите зависимости:
```
pip install -r requirements.txt
```

Создайте файл config.py и задайте в нём базовые переменные:
```
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'data_parser.db')
    SECRET_KEY = "Here your secret key"
```

Для работы Flask-Migrate и создания таблиц базы данных нужно выполнить поочередно команды:

Linux и Mac: 
```
export FLASK_APP=webapp && flask db init
```
```
flask db migrate -m "Описание того, что создаётся"
```
```
flask db upgrade
```

Windows: 
```
set FLASK_APP=webapp && flask db init
```
```
set FLASK_APP=webapp && flask db migrate -m "Specify what has been added or changed"
```
```
flask db upgrade
```

## Для парсинга по расписанию:

Windows:

Установить Linux-подсистему (Ubuntu) для Windows.
В командной строке Windows вызвать Linux-подсистему (Ubuntu) - `wsl`. Далее здесь же:
При первой установке
```
sudo apt-get install redis-server
```
```
sudo systemctl enable redis-server.service
```
В следующий раз начинать с этой строки
```
sudo service redis-server start
```
```
redis-cli
```
```
monitor
```

Запустить celery в отдельной командной строке Windows в папке приложения или окне терминала:
```
celery -A tasks worker -l info --pool=solo
```
Затем можно остановить процесс в Linux-подсистеме `CTRL C` и выйти из неё `CTRL D`.

Чтобы запуск задач по расписанию работал, мы должны запустить celery-beat также в отдельной командной строке Windows в папке приложения или окне терминала:
```
celery -A tasks beat
```


## Запуск программы

Для запуска программы и вывода в браузер запустите файл:

Скрипт для Linux и MacOs

Linux и Mac: 
В корне проекта создайте файл run.sh:
#!/bin/sh
export FLASK_APP=webapp && export FLASK_ENV=development && flask run
Сохраните файл и в корне проекта выполните в консоли команду chmod +x run.sh - это сделает файл исполняемым. Теперь для запуска проекта нужно писать 
```
./run.sh. 
```

Windows:
```
run.bat
```
или 

```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```


Для добавления данных результата парсинга вручную в БД запустите файл `get_all_data.py`.

Для первичного создания таблиц БД запустите файл `create_db.py`
