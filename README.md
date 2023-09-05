### **Test task for Python develope** _Longevity In Time_

### Description

**The project includes the creation of a RESTful API user model using Django Rest Framework (DRF), integration of authentication and authorization, using Auth0 for authentication.**
 
### Functionality

- **The user's model.** User registration, login, user profile acquisition, user profile update and account deletion.
- **Secure password hashing and storage.** Secure password hashing and storage using the Django - Argon hashing algorithm.
- **Validation and Error handling.** Appropriate validation and error handling methods for endpoints are implemented.
- **Custom User model and Authentication.** Custom user model that includes email as a unique identifier.

### Technologies

- Python 3.7
- Django 3.2.20
- Django Rest Framework 3.14.0
- djangorestframework-simplejwt 4.8.0
- djoser 2.1.0
- drf-yasg 1.21.7
- argon2-cffi 23.1.0

###  The project is launched at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/redoc/ - project documentation
- http://127.0.0.1:8000/admin/ - admin page

### Project launch

Clone the repository and navigate to it in the command line:
```sh
git clone https://github.com/DmitryOstrovskiy/LongevityInTime_Test_Tasks && cd LongevityInTime_Test_Tasks
```
Install the virtual environment, activate it and install dependencies:
```sh
python -m venv venv && Windows: ```source venv\scripts\activate```; Linux/Mac: ```sorce venv/bin/activate``` && pip install -r requirements.txt
```
Perform migrations:
```sh
python manage.py migrate
```
Create a superuser:
```sh
python manage.py createsuperuser
```
Start the server:
```sh
python manage.py runserver
```

### Query examples

### _Registration of the user_
**POST**: http://127.0.0.1:8000/api/auth/users/

Request example:
```json
{
"first_name": "Ivan",
"last_name": "Ivanov",
"username": "IvanIvanov",
"password": "UserIvan1",
"email": "ivan@yandex.ru"
} 
```
Response example:
```json
{
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "username": "IvanIvanov",
    "email": "ivan@yandex.ru",
    "id": 2
}
```

### _Getting a JWT token_
**POST**: http://127.0.0.1:8000/api/auth/jwt/create/   
Request example:
```json
{
"email": "ivan@yandex.ru",
"password": "UserIvan1"
}  
```
Response example:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzkyMjE5NCwianRpIjoiOTg0NzFiYTg1MDgyNDIzN2I1NDZjMTYyZTczNzM2MzUiLCJ1c2VyX2lkIjoyfQ.AA7j0s3gdmfPLamYy9FxomsN00zXfs73-8RGkWFWs2E",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzOTIyMTk0LCJqdGkiOiJhZTNiMDM0ZjRmMGQ0MmU5OWJhMGVjNTRiODRlMDQ5OCIsInVzZXJfaWQiOjJ9.Rvcm8ZfiRUGi0XsBglMXLzhQn5jV2L40V53X-RZHQbs"
}
```

### _Getting a user profile_
**GET**: http://127.0.0.1:8000/api/auth/users/2/ - In the Authorization tab, you need to pass an access token
Response example:
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

### _Updating the user profile_
**PUT**: http://127.0.0.1:8000/api/auth/users/2/ - In the Authorization tab, you need to pass an access token
Request example:
```json
{
"first_name": "Ivan",
"last_name": "Ivanov",
"username": "SuperIvan",
"password": "UserIvan1234",
"email": "ivan@yandex.ru"
} 
```
Response example:
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

### _Deleting a user profile_
**DELETE**: http://127.0.0.1:8000/api/auth/users/2/ - In the Authorization tab, you need to pass an access token
Request example:
```json
{
"current_password": "UserIvan1234"
}
```

### Author - Dmitry Ostrovsky

