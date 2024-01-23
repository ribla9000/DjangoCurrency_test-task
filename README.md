**StepByStep**:
1. ```sudo apt install redis```
2. ```redis-server redis.conf```
3. `pip3 install -r requirements.txt`
4. ```sudo -su postgres psql```
5. ```CREATE DATABASE your_database_name WITH OWNER your_owner;```
6. ```\q```
7. `python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver`
8. `celery -A testTask worker -l info --concurrency 1`


Dont forget about:

    1. env_example - There are the variables for the environment.
    2. You must to copy variables from the env_example and add it (with your own values) to the .env in main dir (where is manage.py)