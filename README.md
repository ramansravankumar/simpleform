if we want to access this file
create a floder in that open cmd 
create a virtual environment 
         python3 -m venv env
         go Scripts
         after that activate the environment
         venv\Scripts\activate
1.install django
      python -m pip install django

create a project 
      django-admin startproject test_project
      cd test_project
      after that enter code .
       enter into project
       go to terminal 
         py manage.py startapp appanme
         register appname in settings.py in project level
         INSTALLED_APPS = [
         'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appname'
]
go to app level in that go to models.py 
go to app level create a file forms.py
go to app level go views.py create a views cpoy views above file

after create a html file while display the front-end
   we a folder in project level like name "template"
      after that we create a html file in that by using ".html" extension
      and registor template in settings.py in project level
                  import os
                  TEMPLATE_DIR=os.path.join(BASE_DIR,'template')
                  template=[] in that 'DIRS': [TEMPLATE_DIR],
  go to app level create a urls
               from django.urls import path
               from .views import viewsname before creating the view
               urlpatterns = [ ]
  go to project level urls
                 from django.contrib import admin
                 from django.urls import path,include
                 urlpatterns = [path('admin/', admin.site.urls),path('app1/',include('app1.urls'))]
  makemigrations because we using database  'db.sqlite3'
                              py manage.py makemigrations ,it makes convert 
                              py manage.py migrate ,to execute converted sql code into db
                              if any changes in models compulsary migrations above two commands
    at last runserver command 
                         py manage.py runserver
                        

 


















