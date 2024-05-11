# python language

## what is framwork and what is web framework

## Model View Template
- **model** : database connection and all stuff
in this we process data
insert/update db
communication with database

- **view** : send request to model and send response to template
in view we write :
server side logic
process get post
get data from user
get data from model 
pass data to tamplate

- **template** : user can read and write data from template

#### why we use MVT
organize code
indepedent block
reduce complexity of code and web applicaltion
easy to maintain
easy to modify

## why we need to learn Django
- this is high level framwork
- authentication
- versatile database connection
- ORM
- template engine

## prerequisite
- html
- css
- javascript
- python
- SQL
- MVT
- PIP
- bootstrap

## how to install
1. install vitual environment
- virtualenv install
- create env and run source env/bin/activate
- install django
- pip install django

## structure of django project 
- root directory means : manage.py file is present in which directory this called root directory
- __init__.py : this file consider as python package.
- wsgi.py(web server gatway interface) : this file consider as web server and spacifiy how web server communicate with web application
- asgi.py : this is upgrade of wsgi.py this provides asynchronous web server and syncronus web server
- settings.py : this file contain all setting for django project
- settings.py : this file contain all setting for django project, database config information, template, install application and validator
- urls.py : this file contain all url for django project
- manage.py : this file contain all command for django project

## setting file in django
- DEBUG = True for detail information about problem
- build in application in django
- DATABASES this is for django database connection