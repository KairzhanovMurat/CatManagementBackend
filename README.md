


# Cat Management Backend

Этот проект предоставляет API для онлайн-выставки котят.

## Начало работы

### Предварительные требования

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Клонирование репозитория

```bash
git clone https://github.com/KairzhanovMurat/CatManagementBackend.git

cd CatManagementBackend
```

### Настройка

1. Переименуйте файл `.env.example` в `.env` и задайте ваши переменные окружения.

### Сборка и запуск приложения

```bash
docker-compose up --build -d
```

### Доступ к API

API будет доступно по адресу `http://localhost:8000`.

## Входные данные
- email: example@email.com
- password: password123

### Запуск тестов

Для запуска тестов используйте следующую команду:

```bash
docker-compose exec -it <имя контейнера> pytest
```


