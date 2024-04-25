# easy-buddy
This is a repository for final project Easy Buddy

## Prerequisites
1. Python3 and pip must be installed
2. Postgres with a local deployment must be installed locally

## Setup guide
1. Create an .env file in root directory after cloning the repository
```env
DB_NAME="easy_buddy"
DB_USER="postgres"
DB_PASSWORD="postgres"
DB_HOST="localhost"
DB_PORT=5432
```
2. Create Virtual env and activate
```shell
python3 -m venv .venv
source .venv/bin/activate
```
3. Install pip requirements
```shell
pip3 install -r requirements.txt
```
4. Make and run migrations if done changes to models
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
5. If database is not created follow below steps
```shell
sudo su postgres
psql
postgres-# \l 
#---------Lists databases available, if database is not created create one
postgres-# create database easy_buddy;
postgres-# \l
#---------Verify database is created
postgres-# \q
exit
```
6. Make and run migrations if done changes to models
```shell
python3 manage.py makemigrations <appname>
python3 manage.py migrate
```
7. Run server
```shell
python3 manage.py runserver
```
8. Navigate to http://127.0.0.1:8000/ signup and signin
9. Create a superuser to access admin panel and manage users
```shell
python3 manage.py createsuperuser
Username (leave blank to use 'dci-student'): admin
Email address: admin@gmail.com
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
10. Navigate to http://127.0.0.1:8000/admin. username admin and password admin




