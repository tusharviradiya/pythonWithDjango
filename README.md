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

## how to create application in python
- go to project file 
- run command - python manage.py startapp application_name
- go to project file
- run command - python manage.py runserver
- go to project file
- run command - python manage.py migrate
- go to setting file and add application name in INSTALLED_APPS

## application directory structrure in django
- **migrations** : this directory contain all migration
- **__init__.py** : this file consider as python package
- **models.py** : this file contain all model
- **views.py** : this file contain all view
- **templates** : this directory contain all template
- **static** : this directory contain all static files
- **admin.py** : this file contain all admin panel
- **test.py** : this file contain all test

# view

## create funciton based view in django
- go to project file
- open view file of appication
- write your all business logic in this file 

## singal application with mutliple view funciton
- go to project file
- open view file of appication
- write your all business logic in this file
- and set url in urls.py file

## URL dispatcher
- mapping between url path expression and view functions
- it can referes other mapping

#### path()
- path(route, view, kwargs=None, name=None)
- route should be string
- view should be function
- kwargs is dictionary
- name is string

#### multiple application inside project
- add application in install section and add application name in INSTALLED_APPS

#### include() function
- urlpattern can include other module
- syntext : include(module, namespace=None, app_name=None) or include(pattern_list) or include((pettern_list, app_namespace), namespace = None)