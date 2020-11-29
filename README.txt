Описание
Использвался django-rest-framework для создания rest-api, SQlite в качестве БД

Предварительно:
pip install Django
pip install django-rest-framework
python manage.py runserver - запускаем локальный сервер

http://127.0.0.1:8000/admin - адмика с возможностью создавать вопросы и добавлять их в опросы.
http://127.0.0.1:8000/api/polls - опросы (с прикрепленными вопросами)
http://127.0.0.1:8000/api/questions - список вопросов
http://127.0.0.1:8000/api/answers - просмотр ответов, добавление ответа с параметрами username, answers, связь с опросом и вопросом