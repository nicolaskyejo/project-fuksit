# Project Fuksit

A 'gamified' web-app for introducing first-year students to using the school system OMA.

## Getting Started

How to run the project locally. First clone this repository

```
git clone https://github.com/nicolaskyejo/project-fuksit.git
```

### Prerequisites
1. Python 3.6+
2. Postgres
3. Redis

Installing Postgres and Redis in Arch Linux.
 Use equivalent commands in other flavours of Linux OS. 

```
sudo pacman -S redis postgresql
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'
sudo systemctl enable --now postgresql.service redis.service
sudo su postgres -c psql
```
Then create a new role or skip to the next part if you want to use the
default role.
Replace 'rolename' and 'password' of course.
```
CREATE ROLE rolename WITH
	LOGIN
	NOSUPERUSER
	CREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'password';
```
If you created a new role, replace 'owner' with the role name; Else replace 
'owner' with 'postgres'
```
CREATE DATABASE fuksit
    WITH 
    OWNER = rolename
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
\q
```

### Installing

Set up a virtual environment e.g venv

```
cd project-fuksit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Finally create a .env file with your favorite editor

```
vim .env
```
Write and enter the following values, again replacing
'rolename' and 'password' with previously entered values.
```
SECRET_KEY = 'yoursecretkeythatisreallyimportant'
SQLALCHEMY_DATABASE_URI = 'postgresql://rolename:password@localhost/fuksit'
SESSION_TYPE = 'redis'
SESSION_REDIS = 'redis://:@127.0.0.1:6379'
```
Finally if every step worked without errors,
 launch the web application by
```
python3 wsgi.py
```
Open your favorite browser and navigate to '127.0.0.1:5000'

## How it looks like
<img src="collagesd.png" alt="Demo"/>

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - The web framework used
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Login helper
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Database ORM
* [Flask-Session](https://pythonhosted.org/Flask-Session/)- Server-side session
* [Bootswatch Darkly](https://bootswatch.com/darkly/) - Bootstrap 3

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Cookie warning](https://github.com/wimagguc/jquery-eu-cookie-law-popup)
* [Quiz form layout](https://github.com/mjhea0/thinkful-mentor/blob/master/python/flask-wtf-quiz/quiz_forms.py)
* [XP-bar animation](https://codepen.io/AfroDev/pen/gbXWjQ)
