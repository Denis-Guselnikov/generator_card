# generator_card
Приложение для управления базой данных бонусных карт (карт лояльности, кредитный карт и т.д)

### Функционал:
- Просмотр информации карты
- Редактирование карты
- Удаление карты
- Поиск на странице

# Запуск проекта без Docker

1. ```Клонировать репозиторий https://github.com/Denis-Guselnikov/generator_card```
2. ```cd card_manage/```
3. ```Создаёте виртуальное окружение```
4. ```pip install -r requirements.txt```
5. ```Создать и заполнить .env - файл должен находится в cart_manage```

## Образец:
```
DB_ENGINE=django.db.backends.postgresql  # указываем, что работаем с postgresql
DB_NAME=db_name  # имя базы данных
POSTGRES_USER=db_user  # логин для подключения к базе данных
POSTGRES_PASSWORD=db_password  # пароль для подключения к БД (установите свой)
DB_HOST=db_host  # название сервиса (контейнера)
DB_PORT=5432  # порт для подключения к БД
```
## База Данных

В репозитории есть db.sqlite3

6. ```cd card_manage/```
7. ```python manage.py runserver```

```
login: admin
password: admin
```

# Запуск с помощью Docker

Убедитесь, что вы находитесь в той же директории, где сохранён Dockerfile

1. ```Клонировать репозиторий https://github.com/Denis-Guselnikov/generator_card```
2. ```docker build -t card_manage .```
3. ```docker run --name card_manage -it -p 8000:8000 card_manage```

Проект доступен: ```http://127.0.0.1:8000/```
