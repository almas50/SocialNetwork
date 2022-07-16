### Run 

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Запуск Celery:
```shell
python -m celery -A SocialNetwork worker -l INFO
```
## Запуск Redis:
```shell
redis-server
```
### Swagger
```
http://localhost:8000/api/v1/swagger/
```