# Локальное развертывание проекта

## Общая информация

* Python 3.11
* Django 5.0


# Установка проекта в Docker

[Установка докера](https://www.docker.com/get-started/)

Взаимодействие с проектом происходит с помощью утилиты make

1. Сбилдить образы
```bash
make docker_build
```

2. Поднять postgres
```bash
make docker_postgres
```

3. Поднять Web
```bash
make docker_server
```

4. Применить миграции
```bash
make docker_migrate
```

5. Создать пользователя админки
```bash
make docker_createsuperuser
```

Проект поднимется на http://localhost:8000


# Установка проекта локально

## Docker

База данных поднимается через Docker

[Установка докера](https://www.docker.com/get-started/)

Взаимодействие с проектом происходит с помощью утилиты make

1. Создание Postgres контейнера данных (вывешивается порт 5439)
```bash
make postgres
```

2. Создание базы данных
```bash
make createdb
```

## Установка проекта

1. Скачиваем Python 3.11

2. Создаем виртуальное окружение в директории с проектом
```bash
python3.11 -m venv venv
```

3. Активируем виртуальное окружение
```bash
source venv/bin/activate
```

4. Установка зависимостей
```bash
pip install -r requirements.txt
```

5. Применение миграций
```bash
python manage.py migrate  
```

## Запуск проекта

```bash
make server
```
