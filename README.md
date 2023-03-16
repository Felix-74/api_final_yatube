# Финальный проект API для Yatube
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![Django](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![Django](https://img.shields.io/badge/drf-%23092E20.svg?style=for-the-badge&labelColor=blue&logo=django&logoColor=white)
### Описание
Данный проетк показывает возможности примениения API для работы социальной сети Yatube с пагинацией.
Можно получать список всех публикаций, комментариев, списка доступных сообществ.
Есть возможность отправлять запросы к API, создавать посты, добавлять комментарии и подписываться на авторов
### Установка
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
``` 
Установить и активировать виртуальное окружение:
``` 
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
``` 
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

### Примеры
POST /api/v1/posts/:
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Пример ответа
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
POST /api/v1/posts/{post_id}/comments/:
```
{
    "text": "string"
}
```
Пример ответа
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
---
POST /api/v1/follow/:
```
{
    "following": "string"
}
```
Пример ответа
```
{
    "user": "string",
    "following": "string"
}
```
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&width=435&lines=Igor+Teplov)](https://git.io/typing-svg)