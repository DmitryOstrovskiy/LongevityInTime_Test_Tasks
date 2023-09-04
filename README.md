### **Тестовое задание для Python разработчика** _Longevity In Time_

### Описание

**Проект включает в себя создание RESTful API модели пользователя с помощью Django Rest Framework (DRF), интеграцию аутентификации и авторизации, используется Auth0 для аутентификации.**
 
### Функционал

- **Модель пользователя.** Регистрации пользователя, вход в систему, получение профиля пользователя, обновление профиля пользователя и удаление учетной записи.
- **Безопасное хэширование и хранение паролей** Безопасное хэширование паролей и их хранение с использованием алгоритма хэширования Django - Argon.
- **Валидация и обработка ошибок** Реализованы соответствующие методы валидации и обработки ошибок для эндпоинтов.
- **Кастомная модель пользователя и аутентификация** Кастомная модель пользователя, которая включает электронную почту в качестве уникального идентификатора.

### Технологии

- Python 3.7
- Django 3.2.20
- Django Rest Framework 3.14.0
- djangorestframework-simplejwt 4.8.0
- djoser 2.1.0
- drf-yasg 1.21.7
- argon2-cffi 23.1.0

### Проект запускается по адресу:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/redoc/ - документация к проекту
- http://127.0.0.1:8000/admin/ - страница администратора

### Запуск проекта

Клонируйте репозиторий и перейдите в него в командной строке:
```sh
git clone https://github.com/DmitryOstrovskiy/LongevityInTime_Test_Tasks && cd LongevityInTime_Test_Tasks
```
Установите виртуальное окружение, активируейте его и установите зависимости:
```sh
python -m venv venv && Windows: ```source venv\scripts\activate```; Linux/Mac: ```sorce venv/bin/activate``` && pip install -r requirements.txt
```
Выполните миграции:
```sh
python manage.py migrate
```
Создайте суперпользователя:
```sh
python manage.py createsuperuser
```
Запустите сервер:
```sh
python manage.py runserver
```

### Примеры запросов

### _Регистрация пользователя_
**POST**: http://127.0.0.1:8000/api/auth/users/
Пример запроса:
```json
{
"first_name": "Ivan",
"last_name": "Ivanov",
"username": "IvanIvanov",
"password": "UserIvan1",
"email": "ivan@yandex.ru"
} 
```
Пример ответа:
```json
{
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "username": "IvanIvanov",
    "email": "ivan@yandex.ru",
    "id": 2
}
```

### _Получение JWT-токена_
**POST**: http://127.0.0.1:8000/api/auth/jwt/create/   
Пример запроса:
```json
{
"email": "ivan@yandex.ru",
"password": "UserIvan1"
}  
```
Пример ответа:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzkyMjE5NCwianRpIjoiOTg0NzFiYTg1MDgyNDIzN2I1NDZjMTYyZTczNzM2MzUiLCJ1c2VyX2lkIjoyfQ.AA7j0s3gdmfPLamYy9FxomsN00zXfs73-8RGkWFWs2E",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzOTIyMTk0LCJqdGkiOiJhZTNiMDM0ZjRmMGQ0MmU5OWJhMGVjNTRiODRlMDQ5OCIsInVzZXJfaWQiOjJ9.Rvcm8ZfiRUGi0XsBglMXLzhQn5jV2L40V53X-RZHQbs"
}
```

### _Получение профиля пользователя_
**GET**: http://127.0.0.1:8000/api/auth/users/2/ - Во вкладке Authorization необходимо передать access-токен
Пример ответа:
```json
{
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "username": "IvanIvanov",
    "password": "pbkdf2_sha256$260000$Zn7FJL7NbWZve3dbPbqMGJ$/1EmKlUMQ0SfGGClHnxjrSH4xH8PBekFuJAmBjuO048=",
    "id": 2,
    "email": "ivan@yandex.ru"
}
```

### _Обновление профиля пользователя_
**PUT**: http://127.0.0.1:8000/api/auth/users/2/ - Во вкладке Authorization необходимо передать access-токен
Пример запроса:
```json
{
"first_name": "Ivan",
"last_name": "Ivanov",
"username": "SuperIvan",
"password": "UserIvan1234",
"email": "ivan@yandex.ru"
} 
```
Пример ответа:
```json
{
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "username": "SuperIvan",
    "password": "UserIvan1234",
    "id": 2,
    "email": "ivan@yandex.ru"
}
```

### _Удаление профиля пользователя_
**DELETE**: http://127.0.0.1:8000/api/auth/users/2/ - Во вкладке Authorization необходимо передать access-токен
Пример запроса:
```json
{
"current_password": "UserIvan1234"
}
```

### Автор - Дмитрий Островский

