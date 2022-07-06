# IMDB-API-Clone With DRF (Django Rest Framework)

# Description
This project provide some APIs related to the IMDB platform
The techs in this project 
* Django
* DRF
* Basic Authentication
* JWT Authentiation
*Throttling
* Filtering, Searching, Ordering
* Test Driven development

# How to Install and Run the Project
## Active virtual environtment
Using the  [virtualenv](https://docs.python.org/3/library/venv.html#venv-def)
```
# create a new virtualenv
python3 -m venv venv

# active virtualenv
.\venv\Scripts\activate

# Install library
pip install -r requirements.txt
```

# How to Use the Project

```
cd .\watch_update\
python3 manage.py runserver
```

# Run the test case
```
# in the watch_update folder (in the same level with manage.py file)
# python3 manage.py test <app_name>
# test movies app
python3 manage.py test movies

# test users app
python3 manage.py test users
```

# API document
After run the web server in the local, access the [swagger](http:/localhost:8000/dashboard)
