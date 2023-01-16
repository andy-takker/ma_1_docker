# Домашнее задание

Обернуть приложение в docker-образ и запушить его на Dockerhub.

## Описание

Создать минимальный сервис, который

1. отвечает на порту 8000
2. имеет http-метод
```
GET /health/
RESPONSE: {"status": "OK"}
```

Запушить образ в Dockerhub. На выходе необходимо предоставить:
1. Имя репозитория и тэг на Dockerhub
2. Ссылку на GitHub с Dockerfile, либо приложить Dockerfile в ДЗ
