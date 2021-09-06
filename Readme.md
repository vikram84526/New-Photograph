# Photograph Project

Photograph is a project where user can create image and captions. In this project you do following things -

  - add  user(through admin ).
  - delete user(through admin and api).
  - update user details(image and captions).
  - show all user with their image and captions.
 

# Setup Virtual Environment
  - firstly check if python is not installed in your system then install python.
  - then find the requirements.txt file which is in project outer directory.
  - then create virtual environment using virtualenv myvenv  
  - if virtualenv is not already install in your system then first install virtualenv.
  - then run command " pip install -r requirements.txt " in directory where manage.py file is available.
  
### Activate the Virtualenv 
###### In windows( directory in which myvenv are present)
- env/Scripts/activate

###### In Linux( directory in which myvenv are present)
- source env/bin/activate
- 




## Set up a database

There's a lot of different database software that can store data for your site. We'll use SQLITE

you change the set up in this part of your `NewPhotograph/settings.py` file:


```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```


And we're done! Time to start the web server and see if our website is working!

## Starting the web server

You need to be in the directory that contains the `manage.py` file (the `NewPhotograph` directory). In the console, we can start the web server by running `python manage.py runserver`:


```
(env) D:\vikram\pythontution\Photographs\NewPhotograph>python manage.py runserver
```



Now you need to check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter this address:


```
http://127.0.0.1:8000/
```


## All Important urls
base_url = http://127.0.0.1:8000

- for user create     -- base_url/admin/auth/user/add/
- for user edit       -- base_url/admin/auth/user/3/change/
- for user delete     -- base_url/admin/auth/user/3/delete/
- for userdetails create     -- base_url/admin/custom/userdetails/add/

- for list all userdetails   -- base_url

 
## All api urls 

api_base_url = http://127.0.0.1:8000/api/user/
** pass user's username in place of slug keyword in api's url

- for userdetails edit (through api)       -- api_base_url/<slug>/update/
- for userdetails delete (through api)     -- api_base_url/<slug>/delete/
- for getting token for user api authentication  --  api_base_url/api_login/

## User credentials

##### admin 
username - akash
password - 1234










 


