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

## how to create project in django
- run this cammand : django-admin startproject myproject

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

## url pattern in application 
- first make urls.py file in application 
- after that we need to write url pattern in that file 
- after that we need to inclue in project urls.py file

# Template
- html code where we write in view.py file or there is someting we need to write in template file

## how to write template file in project
- first we need to create template file and create one file in that folder
- after that we need to write render function in view file 
- render() : combine template and data and return an HttpResponse object with that render text
    syntext : render(request, template_name, context=dict_name, content_type=MIME_type, status=None, using=None)

## create folder in template folder for better understanding
- in this we need to give path in perticuler application view.py file

## dynamic tempalte file using DTL
- varialbe : {{variable}}
- in view file we write one dictionory and key is in our template file called
- filter : {{variable|filter_name}} for example : {{name|upper}}
- dot lookup : {{variable.name}} for example : {{name.first}}

## Template inside project
- when we install telmplate in app so we need to APP_DIRS = ture in settings.py
- when we make template normal so we need to focus on TEMLATES_DIRS
- when we make hybrid so we need to inpliment both

## static file
- in static file we need to write path
- {% load static %}
- {% static 'css/style.css' %}
- {% link %}

## static file in root directory
- we need to add STATIC_URL = '/static/' in settings.py
- and STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] also 

## static file in application
- we need to add STATIC_URL = '/static/' in settings.py
- and STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] also   
- we also need to create static folder in application with one file and all file in this 

## template inheritance
- we can inherit template from another template

## extends tag
- {% extends './base.html' %}
- it has no end tag

## block teg
- overriding spacific part of template
- {% block blockname %}......{% endblock blockname%}
- we need to add blockname in template file at first place
- when we need perent tempate content or we also add some content so we add this tag {% block.super %}

## template inheritance with static file 
- we need to add static lode on file and after that we use static on our project

## bootstrap implimentation
- we download bootstrap complile css and js
- after that we copy jsdiliver js file and put it in bootstrap folder

## hyperlink tag
- url tag : {% url 'url_name' %}, {% url 'url_name' as var%}
- example : <a href="{% url 'url_name' %}">click here</a>

## include tag in django
- using this we use multiple time our template
- {% include 'template_name' %}
- {% include 'template_name' with context only %} : in this context only go ahead

## Cookies in django
- means some date which user need everytime

## ORM (object relational mapper)
- give feature to connect any database in django

## QuerySet 
- list of all object which we created using django model
- allow to user to read, filter and order data from database

# Model

## model class
- one class is create table in database

## makemigrations
- propagating change to database
- in simple words makemigrations is convert classes into sql statement

## migrate
- execute sql statements

## sqlmigrate
- display sql statements for migrations

## showmigrations
- list migrations and status
- which migrations is panding is shown here

## all() 
- it return a copy of current QuerySet or subclass

## admin application
- built-in application 
- it provide admin panel for django
- crud operations without writing sql statements
- for this admin pannel makemigrations are already done we need only migrate

## create super user
- command : python3 manage.py createsuperuser

## register table to admin panel
- open application
- opne admin file
- import class in admin file 
- after that admin.site.register(student)

## __str__ method
- it return string representation of object
- by default it return object name and primary key
- why : because when we create any entry so it will return object only at this time we confused about which date is for which object
- we write this in models.py file

## django form
- also called form api 
- bound means form is already filled
- unbound means form is not filled
- form not include form and submit button

## display form to user
- create form.py file and create class for form
- create views.py function and link urls.py file 
- also in project urls file add urls
- make html file for form because there are no form attribute and submit button

## form rendering options
- {{from}}
- {{from.as_table}}
- {{from.as_p}}
- {{from.as_ul}}

## configure id attrubute
- auto_id=False : no id and lable name show in html code
- auto_id=Ture : id and lable name show in html code
- Label_suffix : it add space after label

## ordering form filled
-  fm.order_fields(field_order=['email', 'name']) like this we order our table filds

## loop form 
- {% for field in form %}
    {{field.label_tag}}
  {% endfor %}

## hidden labels 
- weight = label.hidden
- in for loop we write visible_fields()

## get post in form
- in form in method we write get and post 
- post give CSRF protection
- what is CSRF(cross site request forgery) : 


# API part

## what is API
- which stands for Application Programming Interface, acts as a middleman between different software programs. 
- It's a set of rules that defines how applications communicate with each other to exchange data or functionality.

## what is web API ?
- in this web api we need to register first after that we achive one api key for authentication perpose
- using this api key we use that api in out application

## rest api
- it is architectural guideline for building web api
- rest api and restful api are both same only name are differance

## CRUD operations
- create : post
- read : get
- update : put, patch
- delete : delete

## django REST framework
- toolkit for building web api

## installation of Django REST framework()
- pip install djangorestframework
- after that we install django rest framework in our setting file like "rest_framework"

## python json
- if we convert python code into json using json.dumps() method
- if json to python we use loads() method

## serializer and serialization
- serializer used to convert complax data to python datatype
- complax data like queryset or model instance
- this process called serialization

## deserializer and deserialization
- deserializer used to convert python datatype to complax data
- python datatype like list or dictionary
- this process called deserialization
